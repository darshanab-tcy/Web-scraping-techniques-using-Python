import scrapy

class QuotesSpider(scrapy.Spider):
    """
    Simple Scrapy spider to demonstrate structured data scraping.

    Target site: https://quotes.toscrape.com
    Extracts: quote text, author, tags
    """

    name = "quotes_simple"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # Extract structured data from each quote block
        for quote in response.css("div.quote"):
            yield {
                "quote": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("a.tag::text").getall()
            }

        # Handle pagination by following the 'Next' link
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
