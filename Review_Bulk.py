from scrapy.selector import Selector
from scrapy.http import Request
import requests,re

res = requests.get("http://www.comparometer.in/price-list/mobile-phones/apple-iphone-x-3gb-ram-64gb-price-in-india")
data = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div[@class="col s4 reviewrating"]/img/@src').extract()
data2 = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div[@class="col s4 reviewrating"]/span/text()').extract()
data3 = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div[@class="col s4 reviewrating"]/a/@href').extract()

print(data)
print(data2)
print(data3)

a = list(zip(data,data2,data3))
a1= " ".join(str(x) for x in a)
print(a1)
print (type(a1))
