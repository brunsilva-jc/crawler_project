from operator import concat
import scrapy

import scrapy

class Guia_Midia_Spider(scrapy.Spider):
    name = "guia_midia"
    start_urls = [
        #'https://www.guiademidia.com.br/agenciasdenoticias.htm',
        #'https://www.guiademidia.com.br/sites/artes-e-cultura.htm',
        #'https://www.guiademidia.com.br/sites/arquitetura-e-decoracao.htm',
        #'https://www.guiademidia.com.br/sites/automobilismo.htm',
        'https://www.guiademidia.com.br/agronomia/agricultura.htm',
    ]

    def parse(self, response):
       for link in response.xpath('body/main/div/nav/ul/li//a'):
            next_page = link.css('a::attr(href)').get()
            categoria = link.css('a::text').get()
            #yield{'categoria':categoria, 'link':mylink}
            yield response.follow(next_page, callback=self.parse_interno,
            meta={'Categoria': categoria})
           

    def parse_interno(self, response):
        for link in response.xpath('/html/body/table/tr[2]/td/table/tr[1]/td[1]/table/tr[1]/td[2]/table[2]/tr[3]//a'):
            if link.css('a::text').get() and link.css('a::attr(href)').get() is not None:
                title = link.css('a::text').get()
                link = link.css('a::attr(href)').get()
                categoria = response.meta['Categoria']
                yield  {
                    'Categoria': categoria,
                    'title': title,
                    'link': link
                    }
                

    
      
           

