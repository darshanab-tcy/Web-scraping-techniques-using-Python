"""
Playwright-based web scraper for JavaScript-rendered pages.

Target website:
https://quotes.toscrape.com/js/

This script demonstrates:
- JavaScript-rendered content scraping
- DOM-based extraction
- Pagination handling
- Structured data export to CSV

"""

from playwright.sync_api import sync_playwright
import pandas as pd


def launch_browser(playwright, headless=True):
    """
    Launches a Chromium browser instance.

    Args:
        playwright: Playwright instance
        headless (bool): Whether to run browser in headless mode

    Returns:
        Browser object
    """
    return playwright.chromium.launch(headless=headless)


def scrape_quotes_from_page(page):
    """
    Extracts quotes, authors, and tags from the current page DOM.

    Args:
        page: Playwright Page object

    Returns:
        List of dictionaries containing scraped quote data
    """
    quotes_data = []

    # Select all quote blocks on the page
    quote_elements = page.query_selector_all("div.quote")

    for quote in quote_elements:
        text = quote.query_selector("span.text").inner_text()
        author = quote.query_selector("small.author").inner_text()
        tags = [
            tag.inner_text()
            for tag in quote.query_selector_all("a.tag")
        ]

        quotes_data.append({
            "quote": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    return quotes_data


def scrape_all_pages(start_url):
    """
    Scrapes all pages by handling pagination.

    Args:
        start_url (str): Initial URL to start scraping from

    Returns:
        pandas.DataFrame containing all scraped data
    """
    all_quotes = []

    with sync_playwright() as p:
        browser = launch_browser(p, headless=True)
        page = browser.new_page()

        page.goto(start_url)

        while True:
            # Wait until JavaScript renders quote elements
            page.wait_for_selector("div.quote")

            # Scrape current page
            all_quotes.extend(scrape_quotes_from_page(page))

            # Check if a "Next" button exists
            next_button = page.query_selector("li.next a")

            if next_button:
                next_button.click()
            else:
                break

        browser.close()

    return pd.DataFrame(all_quotes)


def save_to_csv(df, output_path):
    """
    Saves the scraped data to a CSV file.

    Args:
        df (pandas.DataFrame): Scraped data
        output_path (str): Output CSV file path
    """
    df.to_csv(output_path, index=False)


def main():
    """
    Main execution function.
    """
    START_URL = "https://quotes.toscrape.com/js/"
    OUTPUT_FILE = "data/quotes_playwright.csv"

    df = scrape_all_pages(START_URL)
    save_to_csv(df, OUTPUT_FILE)

    print(f"Total quotes scraped: {len(df)}")
    print(f"Data saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
