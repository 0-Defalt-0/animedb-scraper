import scrapy


class AnimesSpider(scrapy.Spider):
    name = "animes"
    start_urls = ["https://anidb.net/anime/?h=1&noalias=1&orderby.name=0.1&view=list"]

    def parse(self, response):
        yield{
            'name':response.xpath('//td/text()').get()
        }
