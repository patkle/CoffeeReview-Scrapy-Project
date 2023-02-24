from w3lib.html import remove_tags
from scrapy import Request, Spider


class ReviewsSpider(Spider):
    name = "reviews"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))

    def start_requests(self):
        for i in range(1, self.pages + 1):
            yield Request(f"https://www.coffeereview.com/review/page/{i}/")

    def parse(self, response):
        for item in response.css(".review-template"):
            yield Request(
                item.css(".review-title a::attr(href)").get(),
                callback=self.parse_review,
            )

    def parse_review(self, response):
        yield {
            "url": response.url,
            "title": response.css(".review-title::text").get(),
            "rating": response.css(".review-template-rating::text").get(),
            "roaster": response.css(".review-roaster::text").get(),
            "roaster_location": self._get_next_column_value(response, "Roaster Location:"),
            "coffee_origin": self._get_next_column_value(response, "Coffee Origin:"),
            "roast_level": self._get_next_column_value(response, "Roast Level:"),
            "agtron": self._get_next_column_value(response, "Agtron:"),
            "est_price": self._get_next_column_value(response, "Est. Price:"),
            "review_date": self._get_next_column_value(response, "Review Date:"),
            "aroma": self._get_next_column_value(response, "Aroma:"),
            "acidity_structure": self._get_next_column_value(response, "Acidity/Structure:"),
            "body": self._get_next_column_value(response, "Body:"),
            "flavor": self._get_next_column_value(response, "Flavor:"),
            "aftertaste": self._get_next_column_value(response, "Aftertaste:"),
            "with_milk": self._get_next_column_value(response, "With Milk:"),
            "blind_assessment": remove_tags(response.xpath(".//h2[contains(text(), 'Blind Assessment')]/following-sibling::p").get("")),
            "notes": remove_tags(response.xpath(".//h2[contains(text(), 'Notes')]/following-sibling::p").get("")),
            "bottom_line": remove_tags(response.xpath(".//h2[contains(text(), 'Bottom Line')]/following-sibling::p").get("")),
        }

    def _get_next_column_value(self, response, column_name):
        return response.xpath(f".//td[contains(., '{column_name}')]/following-sibling::td/text()").get("").strip()
