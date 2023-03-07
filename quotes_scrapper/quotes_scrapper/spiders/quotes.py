import scrapy

class QuotesSpider(scrapy.Spider):
   name = 'quotes'
   start_urls = [
      'http://quotes.toscrape.com/'
   ]

   def parse(self, response):
      title = response.xpath('//h1/a/text()').get()
      quotes = response.xpath('//span[@class="text"]/text()').getall()
      top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()

      # In order to save the results as a file we should run "scrapy crawl quotes -o FILE.json or FILE.csv"
      yield {
         'title': title,
         'quotes': quotes,
         'top_ten_tags': top_tags
      }


