<<<<<<< HEAD
import scrapy


class AutoresSpider(scrapy.Spider):
    name = 'autores'
    start_urls = ['https://quotes.toscrape.com/']
    
    def parse(self, response):
        divs = response.css('.quote')
        
        for div in divs:
            autor = div.css('.author::text').get()
            yield{
                'autores':autor
            }
            
        
            
        
        
    
=======
import scrapy


class AutoresSpider(scrapy.Spider):
    name = 'autores'
    start_urls = ['https://quotes.toscrape.com/']
    
    def parse(self, response):
        divs = response.css('.quote')
        
        for div in divs:
            autor = div.css('.author::text').get()
            yield{
                'autores':autor
            }
            
        
            
        
        
    
>>>>>>> 480e631c28b3028277577fccd467825a5dc68ac0
    