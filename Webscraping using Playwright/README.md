# Web Scraping using Playwright

## Overview
This project demonstrates web scraping of **JavaScript-rendered web pages** using Playwright in Python.

Unlike static scraping approaches, Playwright controls a real browser, allowing JavaScript to execute and content to be extracted from the fully rendered DOM.

---

## Objective
- Demonstrate scraping of JavaScript-heavy websites
- Extract structured data from dynamically rendered content
- Handle pagination through browser interaction
- Export scraped data into CSV format

---

## Target Website
https://quotes.toscrape.com/js/

This is a publicly available demo website designed specifically for web scraping practice.

---

## Tools & Libraries
- Python
- Playwright
- Pandas

---

## Project Structure
```
Web scraping using Playwright/
├── playwright_scraper.py
├── requirements.txt
├── data/
│ └── quotes_playwright.csv
└── README.md
```
---

---

## Data Extracted
- Quote text
- Author name
- Associated tags

A sample output file is included in the `data/` directory.

---

## Scraping Approach
- Launch a Chromium browser using Playwright
- Navigate to a JavaScript-rendered page
- Wait for DOM elements to load after JavaScript execution
- Extract structured data from rendered content
- Handle pagination by clicking the “Next” button
- Save the extracted data to a CSV file

---

## How to Run

### Install dependencies
```
python -m pip install -r requirements.txt
python -m playwright install
```
### Execute the scraper
```
python playwright_scraper.py
```
## Output

The script generates the following file:
```
data/quotes_playwright.csv
```
## When to Use Playwright

Playwright is suitable when:

- Website content is rendered using JavaScript

- Data is loaded dynamically after page load

- User-like interactions (clicks, scrolling) are required

Due to higher resource usage, Playwright is used selectively alongside static scraping tools.

## Legal & Ethical Disclaimer

This project is for educational and demonstration purposes only.

All scraping is performed on publicly accessible demo data.
No authentication, private content, or security mechanisms are bypassed.
