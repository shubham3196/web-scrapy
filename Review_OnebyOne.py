from scrapy.selector import Selector
from scrapy.http import Request
import requests,re

def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

res = requests.get("http://www.comparometer.in/price-list/mobile-phones/apple-iphone-6-plus-1gb-ram-16gb-price-in-india")
review = ""
for item in range(1,3):
    try:
        vendor_name = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div['+str(item)+']/img/@src').extract()
        temp_result = ''.join(vendor_name).strip()
        temp_result = re.search('thumbimage/(.*).png', temp_result)
        vendor_name = temp_result.group(1)
        rating_data = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div['+str(item)+']/span/text()').extract()
        rating_data = ''.join(rating_data)
        rating_data = get_num(rating_data)
        link_data = Selector(text=res.text).xpath('//div[@class="col-sm-12"]/div['+str(item)+']/a/@href').extract()
        link_data = ''.join(link_data)
        temp_list = [vendor_name,rating_data,link_data]
        review=review+str(temp_list)
    except Exception as e:
        print (e)
print (review)
print (type(review))
