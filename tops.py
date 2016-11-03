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
csv_file = currentPath + "/csv/TopsDriedFood.csv"

csv_columns = ['ProductID','ProductName','Price','ImgSrc']

#while i<=5:

headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding':'gzip, deflate, sdch', 'Accept-Language':'en-US,en;q=0.8', 
			'Connection':'keep-alive', 'Cookie':'verify=test; ProductHistory=18000; CampaignId=7gnSyGH2uVzS5RFn; TrackingId=xo685LkBlCZ61V7E; ASP.NET_SessionId=02zsmlzqhusrz4fw5xbm50ay; _cbclose30246=1; _uid30246=4454FC3A.3; verify=test; .BACKTOSHOP.=%2fd%2fFreshFood_ReadyToEat; _cbclose=1; _ctout30246=1; _gat=1; _ga=GA1.3.1056241821.1474571447; _dc_gtm_UA-69357131-1=1; visit_time=237', 
			'Host':'www.tops.co.th', 'Upgrade-Insecure-Requests':'1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

x = 1
data = []
while x <= 30:	
	page = requests.get('http://www.tops.co.th/d/DriedFood_ProcessedFood?page='+str(x)+'', headers=headers)

	tree = html.fromstring(page.text)

	#p = tree.xpath('//*[@id="page"]/div[3]/div[2]/div/div[2]/div[2]/text()')

	#p = list(map(str.strip, p))

	#p = [s.replace('฿',"") for s in p]

	i = 1

	while i <= 50:

		q = tree.xpath('//div[@class="product_grid"]/ui/li['+str(i)+']/div[@class="bottom_zone_grid"]/div[@class="product_name"]/h3/a/text()')

		#p = tree.xpath('//div[@class="product_grid"]/ui/li['+str(i)+']/div[2]/div[@class="text_promo font18"]/span/text()')

		#img = tree.xpath('//div[@class="product_grid"]/ui/li['+str(i)+']/div[1]/div[1]/a/img/@src')

		if q == []:
			break

		#q.insert(0,'T'+str(((x-1)*100)+i).zfill(6)+'')

		#q.append(p[0])

		#q.append(img[0])

		data.append(q)
		print (q, "\n")
		i+=1


	if q == []:
		break

	x+=1

print(data)


#csv_data_list = data
#WriteToCSV(csv_file,csv_columns,csv_data_list)