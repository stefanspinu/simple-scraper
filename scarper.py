import scrapy

url = 'https://www.pandashop.md'

data = {}


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = [
        'https://www.pandashop.md/ro/catalog/electronics/orgtech/pc_components/vga_cards/']

    def parse(self, response):
        for card in response.css('.card-inner'):
            card_img = card.css('a').css(
                '.card-img-top').css('.card-img-picture').css('img').attrib['data-src']
            card_title = card.css('.card-body').css('a ::text')
            card_href = card.css('.card-body').css('a').attrib['href']
            card_price = card.css('.card-body').css('.card-footer').css(
                '.card-price').css('.card-price-inner').css('.card-price_curr ::text')
            yield {
                'title': card_title.get(),
                'price': card_price.get(),
                'href': url + card_href,
                'imgs': url + card_img
            }
        for next_page in response.css('a.btn-showmore'):
            yield response.follow(next_page, self.parse)
