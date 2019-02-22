#测试一下爬虫

import sys
import re
from urllib import request, parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

URL = 'http://web.oa.zulong.com/C6/ZuLongFlowModule.Web/Ajax/OvertimeMeal.aspx'
DATA = b'<root><Data><Module>GetABData</Module><Date></Date></Data></root>'

def http_post(url, data):
	response = request.urlopen(url, data=data)
	return response.read()

def main():
	resp = http_post(URL, DATA)
	print(resp)

if __name__ == '__main__':
	main()