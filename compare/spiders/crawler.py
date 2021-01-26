# -*- coding: utf-8 -*-
import scrapy, re, requests, time
from scrapy.selector import Selector
from scrapy import Request
from compare.items import CompareItem

class CrawlerSpider(scrapy.Spider):
    name = 'infiniabot'
    allowed_domains = ["comparometer.in"]
    start_urls = [
        "http://www.comparometer.in/search/?q=apple+iphone+x/"
        ]

    def get_reviews(self, item):
        url = Selector(text=item).xpath('.//a/@href').extract()
        res = ''
        if len(url):
            url = url[0]
            url = url.replace('../../','http://www.comparometer.in/')
            #res = requests.get(url)
            #data = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div[@class="col s4 reviewrating"]/img/@src').extract()
            #data2 = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div[@class="col s4 reviewrating"]/span/text()').extract()
            #data3 = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div[@class="col s4 reviewrating"]/a/@href').extract()
            #addup = list(zip(data,data2,data3))
            #review = " ".join(str(x) for x in addup)
        else:
            review = "NA"
        return url

    def parser(self, response):
        print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        self.logger.info('callback')
        self.logger.info(response)
        yield {'url': response.text}
    
    def get_discount(self, item):
        discount = Selector(text=item).xpath('.//span[@class="discountp"]/text()').extract()
        if len(discount):
            discount = discount[0]
        else:
            discount = "NA"
        return discount

    def get_name(self,item):
        name = Selector(text=item).xpath('.//a/p[@class="prdcttitle"]/text()').extract()
        if len(name):
            name = name[0]
        else:
            name = "NA"
        return name

    def get_image_url(self,item):
        image_url = Selector(text=item).xpath('.//a/img/@src').extract()
        if len(image_url):
            image_url = image_url[0]
        else:
            image_url = "NA"
        return image_url

    def get_originalprice(self,item):
        originalprice = Selector(text=item).xpath('.//div[@class="item-product"]/strike[@class="baseprice"]/text()').extract()
        if len(originalprice):
            originalprice = originalprice[0]
        else:
            originalprice = "NA"
        return originalprice

    def get_saleprice(self,item):
        saleprice = Selector(text=item).xpath('.//div[@class="item-product"]/span[@class="pricename"]/text()').extract()
        if len(saleprice):
            saleprice = saleprice[0]
        else:
            saleprice = "NA"
        return saleprice

    def get_vendor(self,item):
        vendor = Selector(text=item).xpath('.//div[@class="item-product"]/a/span[@class="storesname"]/img/@src').extract()
        if len(vendor):
            vendor = vendor[0]
            temp_result = ''.join(vendor).strip()
            temp_result = re.search('logo_small/(.*)_small.jpg', temp_result)
            vendor = temp_result.group(1)
        else:
            vendor = "NA"
        return vendor                                      
    
    def parse(self, response):
        items={}
        original_items = response.xpath('.//div[@class="col s3 mainprodtdiv "]').extract()
        for item in original_items:
            items['name'] = self.get_name(item)
            items['discount'] = self.get_discount(item)
            items['image_url'] = self.get_image_url(item)
            items['originalprice'] = self.get_originalprice(item)
            items['saleprice'] = self.get_saleprice(item)
            items['vendor'] = self.get_vendor(item)
            yield Request('http://www.comparometer.in/search/?q=apple+iphone+x/', callback=self.parser, dont_filter=True)
            #yield items
            #yield items
