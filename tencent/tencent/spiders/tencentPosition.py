# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
	name = 'tencentPosition'
	allowed_domains = ['tencent.com']

	url = "http://hr.tencent.com/position.php?&start="
	offset = 0
	start_urls = [url + str(offset)]

	def parse(self, response):
		for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
			location = each.xpath("./td[4]/text()").extract()[0]
			workType = each.xpath("./td[2]/text()").extract()[0]
			if location == '北京' and workType.find('技术类') != -1:
				item = TencentItem()
				item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
				item['positionLink'] = "http://hr.tencent.com/" + each.xpath("./td[1]/a/@href").extract()[0]
				item['positionType'] = workType
				item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
				item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
				item['workLocation'] = location
				yield item

		if self.offset < 1680:
			self.offset += 10

		yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
