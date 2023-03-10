import scrapy

class QuotesSpider(scrapy.Spider):
   name = 'quotes'
   start_urls = [
      'http://quotes.toscrape.com/'
   ]
   custom_settings = {
      'FEED_URI': 'quotes.json',
      'FEED_FORMAT': 'json',
      'CONCURRENT_REQUESTS': 24,
      'MEMUSAGE_LIMIT_MB': 2048,
      'MEMUSAGE_NOTIFY_MAIL': ['PJ@test.com'],
      'ROBOTSTXT_OBEY': True,
      'USER_AGENT': 'Pepito Martinez',
      'FEED_EXPORT_ENCODINGS': 'utf-8'
   }

   def parse_only_quotes(self, response, **kwargs):
      if kwargs:
         quotes = kwargs['quotes']
      new_quotes = response.xpath('//span[@class="text"]/text()').getall()
      quotes.extend(new_quotes)

      next_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
      if next_button_link:
         yield response.follow(next_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
      else:
         yield {
            'quotes': quotes
         }



   def parse(self, response):
      title = response.xpath('//h1/a/text()').get()
      quotes = response.xpath('//span[@class="text"]/text()').getall()
      top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()


      top = getattr(self, 'top', None)
      if top:
         top = int(top)
         top_tags = top_tags[:top]

      # In order to save the results as a file we should run "scrapy crawl quotes -o FILE.json or FILE.csv"
      yield {
         'url': response.url,
         'title': title,
         'top_tags': top_tags
      }

      next_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
      if next_button_link:
         yield response.follow(next_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})

