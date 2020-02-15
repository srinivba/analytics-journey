import scrapy

class BricketSpider (scrapy.Spider):
    name = "bricket_spider"
    start_urls = ["http://brickset.com/sets/year-2016"]
