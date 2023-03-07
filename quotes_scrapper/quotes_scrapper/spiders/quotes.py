import scrapy

class QuotesSpider(scrapy.Spider):
   name = 'quotes'
   start_urls = [
      'http://quotes.toscrape.com/'
   ]

   def parse(self, response):
      print('*' * 10, '\n')
      print(response.status, response.headers)
      print('\n', '*' * 10)

      title = response.xpath('//h1/a/text()').get()
      print(f'Titulo: {title}')

      quotes = response.xpath('//span[@class="text"]/text()').getall()
      for quote in quotes:
         print(f'- {quote}\n')

      top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
      for tag in top_tags:
         print(f'- {tag}\n')


