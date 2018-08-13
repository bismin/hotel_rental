# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from hotel_rental.items import HotelRentalItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['hotels.com']
    start_urls = ['https://in.hotels.com/search.do?resolved-location=CITY%3A689295%3AUNKNOWN%3AUNKNOWN&destination-id=689295&q-destination=Cochin,%20India&q-check-in=2018-08-30&q-check-out=2018-08-31&q-rooms=1&q-room-0-adults=2&q-room-0-children=0']
 
    def parse(self, response):
	product = response.xpath('//*[@id="listings"]/ol/li')
	for job in product:
	  item=HotelRentalItem()
	  item['name']=job.xpath('article/div/div[1]/h3/a/text()').extract_first()
	  item['price']=job.xpath('article/div/div[3]/div[1]/a/span/ins/text()').extract_first()
       	  if(item['price']==None):
		item['price']=job.xpath('article/div/div[3]/div[1]/a/b/text()').extract_first()
			
	  yield item
