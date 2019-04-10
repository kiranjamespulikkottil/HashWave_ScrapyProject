import scrapy

class GlobaltradeSpider(scrapy.Spider):
    name = "globaltrade"

    start_urls = [
            'https://www.globaltrade.net/expert-service-provider.html',
            ]

    def parse(self, response):

        for href in response.css('.sp_country_71 ::attr(href)'):
            yield response.follow(href, self.parse)

        for href in response.css('.sp-image a::attr(href)'):
            yield response.follow(href, self.parse_response)

        for href in response.css('.nav-page a::attr(href)'):
            yield response.follow(href, self.parse)


    def parse_response(self, response):
        yield {
                'log_url' : response.css('.image img::attr(data-original)').get(),
                'title' : response.css('.sp-title span::text').get(),
                'sub_title': response.css('span.sub ::text').get(),
                'primary_location' : response.css('.profile-details td span::text')[1].get(),
                'area_of_expertise' : response.css('.mainExp ::text').get(),
                'about' : response.css('.section table p::text').getall(),
                'website' : response.css('.section table tr a::text').re(r'http.*'),
                'language_spoken' : response.css('.section table tr ::text')[20:55].re(r'\n.{4,8}\n'),
                'page_url' : response.url,
            }
