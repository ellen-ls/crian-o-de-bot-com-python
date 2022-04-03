<<<<<<< HEAD
from unicodedata import name
import scrapy

class TagsSpider(scrapy.Spider):
    name = 'tag'
    start_urls = ['https://quotes.toscrape.com/']
    def parse(self, response):
        
        divs = response.css('.quote')
        
        for div in divs:
            tags = div.css('.tag::text').getall()
            yield{
                'tag':tags
            }
            
=======
from unicodedata import name
import scrapy

class TagsSpider(scrapy.Spider):
    name = 'tag'
    start_urls = ['https://quotes.toscrape.com/']
    def parse(self, response):
        
        divs = response.css('.quote')
        
        for div in divs:
            tags = div.css('.tag::text').getall()
            yield{
                'tag':tags
            }
            
>>>>>>> 480e631c28b3028277577fccd467825a5dc68ac0
        