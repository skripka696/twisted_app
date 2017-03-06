from wssc.wssc.spiders.wssc import QuotesSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
from cgi import parse_qs
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

import os


html = """<html>
   <body>

      <form action = "http://localhost:8080/" method = "post">
         <p>Press the button to start the spider</p>
         <p><input type = "submit" value = "submit" /></p>
      </form>

   </body>
</html>"""

html2 = """<html>
   <body>

      Spider finished

   </body>
</html>"""


class Shortly:
    def __init__(self):
        self.router = UrlRouter()

    def __call__(self, environ, start_respons):
        start_respons('200 OK', [('Content-Type', 'text/html')])
        return [self.router.dispatch(environ)]


class UrlRouter:
    dictionary = {}

    def _parse_env(self, environ):
        return {'method': environ['REQUEST_METHOD']}

    def is_valid_url(self, url):
        res = urlparse.urlparse(url)
        return res.scheme in ('http', 'https')

    def run_spider(self):
        print('dfsdasdsafs')
        spider = QuotesSpider()
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(spider)
        process.start()

    def dispatch(self, environ):
        r_d = self._parse_env(environ)
        if r_d['method'] == 'GET':
            return html.encode('utf-8')
        elif r_d['method'] == 'POST':
            # os.system('python ./run_spider.py')
            reactor.callInThread(self.run_spider)
            return html2.encode('utf-8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, Shortly())
    srv.serve_forever()