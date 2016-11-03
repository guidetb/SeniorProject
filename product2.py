from lxml import html
import requests
import urllib.request
import re
import csv
import os

def WriteToCSV(csv_file,csv_columns,data_list):
	try:
		with open(csv_file, 'w', errors = 'ignore') as csvfile:
			writer = csv.writer(csvfile, dialect = 'excel', quoting = csv.QUOTE_NONNUMERIC)
			writer.writerow(csv_columns)
			for data in data_list:
				writer.writerow(data)
	except IOError as err:
			print("I/O error({0}): {1}".format(errno, streeeoe))
	return


currentPath = os.getcwd()
csv_file = currentPath + "/csv/BigC/PetEquip.csv"

csv_columns = ['ProductID','ProductName','Price','ImgSrc','SubCate','Cate']

#while i<=5:

headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'en-US,en;q=0.8'
			,'Cache-Control':'max-age=0','Connection':'keep-alive','Cookie':'splashpage_confirm=splashpage; _ga=GA1.3.1731975964.1472531847; frontend=bej8jsj6ujmo7kslk0ao33lea2',
			'Host':'www.bigc.co.th','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

x = 1
data = []
while x <= 30:	
	page = requests.get('http://www.bigc.co.th/pet-outdoor-etc/pets/pet-toy.html?limit=100&p='+str(x)+'', headers=headers)

	tree = html.fromstring(page.text)

	p = tree.xpath('//div[@class="regular-price"]/span[@class="price"]/text()|//p[@class="special-price"]/span[@class="price"]/text()')

	p = list(map(str.strip, p))

	p = [s.replace('฿',"") for s in p]

	i = 1

	while i <= 100:

		q = tree.xpath('//*[@id="catalog-category-products"]/ul/li['+str(i)+']/div[2]/h2/a/text()')

		img = tree.xpath('//*[@id="catalog-category-products"]/ul/li['+str(i)+']/div[1]/a/img/@src')

		if q == []:
			break

		q.insert(0,'B'+str(((x-1)*100)+i+6592).zfill(6)+'')

		q.append(p[(i-1)])

		q.append(img[0])

		q.append('SCat0002211')

		q.append('Cat0002206')

		data.append(q)
		print (q, "\n")
		i+=1


	if q == []:
		break

	x+=1

print(data)


csv_data_list = data
WriteToCSV(csv_file,csv_columns,csv_data_list)
#p = tree.xpaht('//span[@class="price"]/text()')

#print (p, "\n")

#pagefile = urllib.request.urlopen("http://www.bigc.co.th/food.html?limit=100")

#htmltext = pagefile.read().decode('utf-8')

#regex = '฿([0-9]{1,4}\.[0-9][0-9])</span>'

#pattern = re.compile(regex)

#price = re.findall(pattern,htmltext)

#print(price, "\n")

#2358