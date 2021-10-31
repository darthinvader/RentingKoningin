import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from funda.items import FundaItem


class MySpider(CrawlSpider):
    name = 'funda'
    allowed_domains = ['funda.nl']
    start_urls = ['https://www.funda.nl/en/huur/hilversum/0-2200/6+slaapkamers/+45km/']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(restrict_xpaths=(
            '//a[@rel="next"]',))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(
            restrict_xpaths=('//div[@class="search-content-output"]/ol/li//div[@class="search-result-media"]/a',)),
            callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = ItemLoader(item=FundaItem(), response=response)

        item.add_value('link', response.url)

        address = response.xpath('//span[@class="object-header__title"]/text()').get().replace('\r', '').replace('\n',
                                                                                                                 '')
        item.add_value('address', address)

        street = response.xpath('//span[@class="object-header__subtitle fd-color-dark-3"]/text()').get().replace('\r',
                                                                                                                 '').replace(
            '\n', '')
        item.add_value('street', street)

        livingArea = response.xpath(
            '(//span[@class="kenmerken-highlighted__value fd-text--nowrap"])[1]/text()').re_first(r'[0-9]+')
        item.add_value('livingArea', livingArea)
        bedrooms = response.xpath(
            '(//span[@class="kenmerken-highlighted__value fd-text--nowrap"])[2]/text()').re_first(r'[0-9]+')
        item.add_value('bedrooms', bedrooms)
        price = response.xpath('(//strong[@class="object-header__price"])/text()').re_first(r'[0-9,]+').replace(',', '')
        item.add_value('price', price)
        deposit = response.xpath('//dt[text()="Deposit"]/parent::*//dd/text()').re_first(r'[0-9,]+').replace(',', '')
        item.add_value('deposit', deposit)

        return item.load_item()
