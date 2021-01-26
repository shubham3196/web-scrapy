# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompareItem(scrapy.Item):
    product_name = scrapy.Field()
    product_discount = scrapy.Field()
    product_image_url = scrapy.Field()
    product_original_price = scrapy.Field()
    product_selling_price = scrapy.Field()
    product_vendor = scrapy.Field()
    product_url = scrapy.Field()
    pass

