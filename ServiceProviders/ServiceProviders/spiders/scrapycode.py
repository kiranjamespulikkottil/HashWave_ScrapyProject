import scrapy

class GlobaltradeSpider(scrapy.Spider):
    name = "globaltrade"

    start_urls = [
            'https://www.globaltrade.net/international-trade-import-exports/expert-service-provider-p/Fastfix-Inc.html',
            ]

    def parse(self, response):
        yield {
                'log_url' : response.css('.image img::attr(data-original)').get(),
                'title' : response.css('.sp-title span::text').get(),
                'page_url' : response.url,
            }
