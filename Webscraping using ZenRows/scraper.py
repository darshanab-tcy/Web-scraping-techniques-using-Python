"""
ZenRows-based web scraping demo.

This script demonstrates how to use ZenRows as an access layer
to fetch HTML content from a website, parse it using BeautifulSoup,
and conditionally store extracted data.

Target sites used are public demo domains (e.g., example.com)
to validate ZenRows integration under trial account constraints.
"""

import os
import csv
import requests
from typing import List, Dict
from bs4 import BeautifulSoup
from dotenv import load_dotenv


class ZenRowsClient:
    """
    Client responsible for fetching HTML content via the ZenRows API.

    This class abstracts all interaction with ZenRows, allowing the
    scraping and parsing logic to remain independent of anti-bot
    protection, proxy rotation, and JavaScript rendering.
    """

    BASE_URL = "https://api.zenrows.com/v1/"

    def __init__(self, api_key: str, js_render: bool = False, timeout: int = 30):
        """
        :param api_key: ZenRows API key
        :param js_render: Whether JavaScript rendering is required
        :param timeout: Request timeout in seconds
        """
        self.api_key = api_key
        self.js_render = js_render
        self.timeout = timeout

    def fetch_html(self, target_url: str) -> str:
        """
        Fetches HTML content for a given URL using ZenRows.

        :param target_url: URL of the target webpage
        :return: HTML content as a string
        :raises: requests.HTTPError if the request fails
        """
        params = {
            "apikey": self.api_key,
            "url": target_url,
            "js_render": str(self.js_render).lower(),
            "premium_proxy": "true"
        }

        # External API call to ZenRows (handles anti-bot, proxies, JS rendering)
        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=self.timeout
        )
        response.raise_for_status()

        return response.text


class QuoteParser:
    """
    Parses quote data from HTML content.
    """

    def parse(self, html: str) -> List[Dict[str, str]]:
        """
        Extracts quotes and authors from HTML.

        :param html: Raw HTML content
        :return: List of dictionaries containing quote data
        """
        soup = BeautifulSoup(html, "html.parser")
        results: List[Dict[str, str]] = []

        for quote_block in soup.select(".quote"):
            quote_text = quote_block.select_one(".text")
            author = quote_block.select_one(".author")

            if quote_text and author:
                results.append({
                    "quote": quote_text.get_text(strip=True),
                    "author": author.get_text(strip=True)
                })

        return results


class CSVWriter:
    """
    Writes structured data to a CSV file.
    """

    def write(self, data: List[Dict[str, str]], file_path: str) -> None:
        """
        Writes a list of dictionaries to a CSV file.

        :param data: Extracted data
        :param file_path: Output CSV file path
        """
        if not data:
            return

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class QuoteScraper:
    """
    Orchestrates the end-to-end scraping workflow.
    """

    def __init__(
        self,
        client: ZenRowsClient,
        parser: QuoteParser,
        writer: CSVWriter
    ):
        """
        :param client: ZenRows client for fetching HTML
        :param parser: Parser for extracting structured data
        :param writer: Writer for persisting results
        """
        self.client = client
        self.parser = parser
        self.writer = writer

    def run(self, url: str, output_file: str) -> None:
        """
        Executes the scraping pipeline.

        :param url: Target webpage URL
        :param output_file: Output CSV file path
        """
        html = self.client.fetch_html(url)
        parsed_data = self.parser.parse(html)   
        self.writer.write(parsed_data, output_file)


def main() -> None:
    """
    Application entry point.
    """
    load_dotenv()

    api_key = os.getenv("ZENROWS_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ZENROWS_API_KEY not found. Please set it in the environment variables."
        )

    zenrows_client = ZenRowsClient(
        api_key=api_key,
        js_render=True  # Enable only if the site requires JavaScript rendering
    )

    parser = QuoteParser()
    writer = CSVWriter()
    scraper = QuoteScraper(zenrows_client, parser, writer)

    scraper.run(
        url="https://example.com",
        output_file="quotes.csv"
    )


if __name__ == "__main__":
    main()
