import scrapy


class QuotesSpider(scrapy.Spider):
    name = "wssc"
    start_urls = ['https://my.wsscwater.com/',]

    def parse(self, response):
        print('hello'.encode('utf-8'))
