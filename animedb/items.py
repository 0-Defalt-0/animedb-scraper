# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose,TakeFirst

def clean_name(inp):
    return inp[0].split('Anime:')[1].strip()

def clean_desc(inp):
    for items in inp:
        inp[inp.index(items)] = items.strip()
    
    text = tuple(inp)
    desc = ''.join(text)

    return desc

def clean_episodes(inp):
    for items in inp:
        inp[inp.index(items)] = items.strip()
        if items.strip() == '':
            inp.remove(items)

    return inp    

class AnimedbItem(scrapy.Item):
    name = scrapy.Field(
        input_processor = Compose(clean_name),
        output_processor = TakeFirst()
    )
    start_date = scrapy.Field(
        output_processor = TakeFirst()
    )
    end_date = scrapy.Field(
        output_processor = TakeFirst()
    )
    tags = scrapy.Field()
    description = scrapy.Field(
        output_processor = Compose(clean_desc)
    )
    episodes = scrapy.Field(
        output_processor = TakeFirst()
    )
    image = scrapy.Field(
        output_processor = TakeFirst()
    )
    additional_tags = scrapy.Field()
    episode_names = scrapy.Field(
        input_processor = Compose(clean_episodes)
    )