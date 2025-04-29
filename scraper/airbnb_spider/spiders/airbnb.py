import scrapy
import json
import requests

class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'

    def start_requests(self):
        url = "https://www.airbnb.com/s/New-York--NY--United-States/homes"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        listings = response.css('div[data-testid="property-card"]')
        for listing in listings:
            data = {
                "title": listing.css('span[aria-label]::text').get(default=''),
                "location": "New York",
                "address": "",
                "price_per_night": float(listing.css('span[class*="price"]::text').re_first(r'\$(\d+)') or 0),
                "currency": "USD",
                "total_price": 0,
                "image_urls": [listing.css('img::attr(src)').get()],
                "ratings": float(listing.css('[aria-label*="Rating"]::text').re_first(r'(\d+\.\d+)') or 0),
                "description": "",
                "num_reviews": int(listing.css('[aria-label*="reviews"]::text').re_first(r'(\d+)') or 0),
                "amenities": [],
                "host": {"name": "John Doe", "is_superhost": True},
                "property_type": "Apartment"
            }

            headers = {"Content-Type": "application/json"}
            response = requests.post("http://localhost:8000/api/add_listing", json=data, headers=headers)
            print(response.status_code, response.text)