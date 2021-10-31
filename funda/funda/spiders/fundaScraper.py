import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from funda.items import FundaItem


class MySpider(CrawlSpider):
    name = 'funda'
    allowed_domains = ['funda.nl']
    start_urls = ['https://www.funda.nl/en/huur/hilversum/0-2200/6+slaapkamers/+100km/']

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
        # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item.add_xpath('address1', '//span[@class="object-header__title"]/text()')
        item.add_xpath('street', '//span[@class="object-header__subtitle fd-color-dark-3"]/text()')
        item.add_xpath('livingArea', '(//span[@class="kenmerken-highlighted__value fd-text--nowrap"])[1]/text()')
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
        item.add_value('url', response.url)
        return item.load_item()
