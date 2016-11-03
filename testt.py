from lxml import html
import requests
import urllib.request
import re
import csv
import os

#while i<=5:

headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'en-US,en;q=0.8'
			,'Cache-Control':'max-age=0','Connection':'keep-alive','Cookie':'splashpage_confirm=splashpage; _ga=GA1.3.1731975964.1472531847; frontend=bej8jsj6ujmo7kslk0ao33lea2',
			'Host':'www.bigc.co.th','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

i = 1
	
page = requests.get('http://www.bigc.co.th/food.html?limit=100', headers=headers)

tree = html.fromstring(page.text)

while i <= 100:

	q = tree.xpath('//*[@id="catalog-category-products"]/ul/li['+str(i)+']/div[1]/a/img/@src')

#q = list(map(str.strip, q))

#q = [s.replace('฿',"") for s in q]

#data.append(q)
	print (q, "\n")
	i+=1

#print(data)   