# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose, TakeFirst
from scrapy.loader import ItemLoader

class FundaItem(scrapy.Item):
    link = scrapy.Field()

    address = scrapy.Field()
    street = scrapy.Field()

    livingArea = scrapy.Field()

    price = scrapy.Field()
    deposit = scrapy.Field()

    last_updated = scrapy.Field(serializer=str)

class FundaLoader(ItemLoader):
    link_out = Compose(TakeFirst())

    address_out = Compose(TakeFirst())
    street_out = Compose(TakeFirst())

    livingArea_out = Compose(TakeFirst())

    price_out = Compose(TakeFirst())
    deposit_out = Compose(TakeFirst())
