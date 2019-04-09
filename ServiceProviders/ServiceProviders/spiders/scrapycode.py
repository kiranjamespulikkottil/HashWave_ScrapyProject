import scrapy

class GlobaltradeSpider(scrapy.Spider):
    name = "globaltrade"

    start_urls = [
            'https://www.globaltrade.net/United-States/expert-service-provider.html',
            ]

    def parse(self, response):
        for href in response.css('.sp-image a::attr(href)'):
            yield response.follow(href, self.parse_response)


    def parse_response(self, response):
        yield {
                'log_url' : response.css('.image img::attr(data-original)').get(),
                'title' : response.css('.sp-title span::text').get(),
                'page_url' : response.url,
            }
