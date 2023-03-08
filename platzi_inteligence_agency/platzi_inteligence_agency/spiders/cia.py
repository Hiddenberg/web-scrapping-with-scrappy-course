import scrapy

# xpaths

class SpiderCIA(scrapy.Spider):
   name = 'cia'
   start_urls = [
      'https://www.cia.gov/readingroom/historical-collections'
   ]
   custom_settings = {
      'FEED_URI': 'cia.json',
      'FEED_FORMAT': 'json',
      'FEED_EXPORT_ENCODING': 'utf-8'
   }

   def parse(self, response):
      XPATH_LINKS = '//div[@class="field-items"]//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]//@href'

      declasified_links = response.xpath(XPATH_LINKS).getall()
      
      for link in declasified_links:
         yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})
   
   def parse_link(self, response, **kwargs):
      XPATH_TITLE = '//h1[@class="documentFirstHeading"]/text()'
      XPATH_BODY = '//div[contains(@class, "field-item")]/p[not(child::strong)]//text()'

      link = kwargs['url']
      title = response.xpath(XPATH_TITLE).get()
      paragraphs = response.xpath(XPATH_BODY).getall()

      yield {
         'url': link,
         'title': title,
         'body': paragraphs
      }