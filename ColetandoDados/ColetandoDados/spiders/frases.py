import scrapy

class FrasesSpider(scrapy.Spider):
    name = 'frases'
    start_urls = ['https://quotes.toscrape.com/']
    def parse(self, response):
        #print(response.css('.quote'))
        divs = response.css('.quote')
                 
        for div in divs:
            frase = div.css('.text ::text').get()
            yield{
                'frase':frase
            }
            
            