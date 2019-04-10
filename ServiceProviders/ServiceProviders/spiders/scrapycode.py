import scrapy

class GlobaltradeSpider(scrapy.Spider):
    name = "globaltrade"

    start_urls = [
            'https://www.globaltrade.net/expert-service-provider.html',
            ]

    def parse(self, response):

        #Follow the link to Service Providers in the United States
        for href in response.css('.sp_country_71 ::attr(href)'):
            yield response.follow(href, self.parse)

        #Follow the link to Service Provider Pages
        for href in response.css('.sp-image a::attr(href)'):
            yield response.follow(href, self.parse_response)

        #Follow Pagination Link
        for href in response.css('.nav-page a::attr(href)'):
            yield response.follow(href, self.parse)


    def parse_response(self, response):
        yield {
                'log_url' : response.css('.image img::attr(data-original)').get(),
                'title' : response.css('.sp-title span::text').get(),
                'sub_title': response.css('span.sub ::text').get(),
                'primary_location' : response.css('.profile-details td span::text').getall(),
                'area_of_expertise' : response.css('.mainExp ::text').get(),
                'about' : response.css('.section table p::text').getall(),
                'website' : response.css('.section table tr a::text').re(r'http.*'),
                'language_spoken' : response.css('.section table tr ::text').re(r'\n.{4,8}\n'),
                'page_url' : response.url,
            }

#Command for Run the Spider : "scrapy crawl globaltrade -o dataset.json"
