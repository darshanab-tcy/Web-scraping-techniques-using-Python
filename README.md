# Web Scraping using BeautifulSoup and Scrapy

This repository demonstrates web scraping techniques using **BeautifulSoup** and **Scrapy** in Python.  
The project focuses on extracting structured data from a publicly available website and exporting it to CSV format.

---

## Objectives
- Demonstrate static web scraping using BeautifulSoup.
- Implement pagination handling.
- Demonstrate scalable scraping using Scrapy.
- Store scraped data in structured CSV files.

---

## Website Used
- https://quotes.toscrape.com  
This website is intended for scraping practice and does not require authentication.
---

## Tools & Libraries
- Python
- BeautifulSoup
- Requests
- Scrapy
- Pandas
- Jupyter Notebook

---

## Project Structure 
---

## BeautifulSoup Scraping
- Sends HTTP requests to static web pages.
- Parses HTML using BeautifulSoup.
- Extracts quote text, author, and tags.
- Handles pagination by detecting "Next" links.
- Saves results to CSV using Pandas.

---

## Scrapy Scraping
- Uses Scrapy spider for structured crawling.
- Automatically handles pagination.
- Faster and more scalable than manual scraping.
- Outputs data directly to CSV.

---

## Output Data
- Quote text
- Author name
- Associated tags

---

## Notes
- This project focuses on **static web scraping**.
- No browser automation was used.

---

## Key Takeaways
- BeautifulSoup is suitable for simple to medium scraping tasks.
- Scrapy is preferred for larger, scalable scraping pipelines.
- Proper project structure and version control are essential.

## CAPTCHA-Aware Scraping (Exploratory)

This repository also includes an **exploratory CAPTCHA-aware scraping module** located in:

`Captcha solver scraper/`

This module demonstrates:
- CAPTCHA detection in scraping workflows
- Integration points for third-party solver services (e.g., 2Captcha)
- Request retry logic after CAPTCHA resolution

📄 Detailed documentation for this module is available in the  
**README inside the `Captcha solver scraper` folder**.
