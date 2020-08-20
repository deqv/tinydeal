import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    # When spider is executed, a request is sent to the following url
    start_urls = ['https://www.tinydeal.com/specials.html']

    # The spider's response is then parsed in the following parse method
    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discounted_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
            }

        # After the response is parsed, the next page link is extracted
        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        # If a next page exists, a request is sent to re-execute the parse method
        if next_page:
            yield scrapy.Request(url-next_page, callback=self.parse)
