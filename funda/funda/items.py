# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundaItem(scrapy.Item):
    link = scrapy.Field()

    address = scrapy.Field()
    street = scrapy.Field()

    livingArea = scrapy.Field()
    bedrooms = scrapy.Field()

    price = scrapy.Field()
    deposit = scrapy.Field()
    rentalAgreement = scrapy.Field()

    last_updated = scrapy.Field(serializer=str)
