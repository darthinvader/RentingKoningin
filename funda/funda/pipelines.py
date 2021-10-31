# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import json


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('houses.json', 'a+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        book = json.dumps(dict(item)) + "\n"
        self.file.write(book)
        return item