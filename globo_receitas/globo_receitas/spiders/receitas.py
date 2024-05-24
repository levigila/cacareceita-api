import scrapy


class ReceitasSpider(scrapy.Spider):
    name = 'receitas'
    allowed_domains = ['panelinha.com.br']
    start_urls = ['https://panelinha.com.br/busca?menu%5Bpage_type%5D=&refinementList%5Bcategories%5D=&page=1&configure%5BhitsPerPage%5D=12']

    def parse(self, response):
        aprendiz= 
        minichef= 
        subchef= 
        chef= 
        confeiteiro= 
        vegano= 
        pass
