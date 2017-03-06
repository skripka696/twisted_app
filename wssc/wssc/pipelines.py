# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class WsscPipeline(object):
    def __init__(self):
        dispatcher.connect(self.close_spider, signals.engine_stopped)

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        pass
