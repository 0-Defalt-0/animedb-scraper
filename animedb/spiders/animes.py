import scrapy
from scrapy.loader import ItemLoader
from ..items import AnimedbItem

class AnimesSpider(scrapy.Spider):
    name = "animes"
    
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://anidb.net/anime/?h=1&noalias=1&orderby.name=0.1&view=list",
            headers=self.HEADERS,
            callback=self.parse
        )


    def parse(self, response):
        links = response.xpath('//td[@data-label="Title"]/a/@href').getall()
        for link in links:
            absolute_link = f"https://anidb.net{link}"
            yield scrapy.Request(
                url=absolute_link,
                headers=self.HEADERS,
                callback=self.parse_anime
            )

        next_page = response.xpath('(//li[@class="next"])[1]/a/@href').get()
        if next_page:
            link = f"https://anidb.net{next_page}"
            yield scrapy.Request(
                url=link,
                headers=self.HEADERS,
                callback=self.parse
            )

    
    def parse_anime(self, response):
        l = ItemLoader(item=AnimedbItem(), response=response)
        l.add_xpath('name','//h1[@class="anime"]/text()')
        l.add_xpath('start_date','//span[@itemprop="startDate"]/@content')
        l.add_xpath('end_date','//span[@itemprop="endDate"]/@content')
        l.add_xpath('tags','//span[@itemprop="genre"]/text()')
        l.add_xpath('description','//div[@itemprop="description"]/text()')
        l.add_xpath('episodes','//span[@itemprop="numberOfEpisodes"]/text()')
        l.add_xpath('image','//div[@class="image"]//img/@src')
        l.add_xpath('additional_tags','//div[@id="tabbed_pane_main_4"]//span[@class="tagname"]/text()')
        l.add_xpath('episode_names','//table[@id="eplist"]//td[@class="title name episode"]/label/text()')

        item = l.load_item()
        yield item