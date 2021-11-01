from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from funda.items import FundaItem, FundaLoader


class MySpider(CrawlSpider):
    name = 'pararius'
    allowed_domains = ['pararius.com']
    start_urls = ['https://www.pararius.com/apartments/hilversum/0-2000/radius-50/page-52']

    rules = (
        # Rule(LinkExtractor(restrict_xpaths=(
        #     '//a[@data-action="click->pagination#onClick" and text()="Next"]',))),

        Rule(LinkExtractor(
            restrict_xpaths=('//ul[@class="search-list"]/li//h2/a',)),
            callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = FundaLoader(item=FundaItem(), response=response)

        item.add_value('link', response.url)

        item.add_value('address', "")

        street = response.xpath('//div[@class="listing-detail-summary__location"]/text()').get()
        item.add_value('street', street)

        living_area = response.xpath(
            '//ul[@class="illustrated-features illustrated-features--compact"]/li[1]/text()').re_first(r'[0-9]+')
        item.add_value('livingArea', living_area)

        item.add_value('price', "")
        item.add_value('deposit', "")

        return item.load_item()
