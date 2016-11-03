import json
import requests
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
csv_file = currentPath + "/csv/tesco/FoodWraps.csv"

csv_columns = ['ProductID','ProductName','Price','ImgSrc','SubCate','Cate']
headers = {
			'accept' : 'application/json', 'Accept-Encoding': 'gzip, deflate, sdch, br', 'Accept-Language': 'en-US,en;q=0.8',
			'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'content-type': 'application/json', 'Cookie': '_csrf=25kTKGDmClZdAuMjM_QTqEyo; AMCVS_1BB646735278569C0A490D45%40AdobeOrg=1; AMCV_1BB646735278569C0A490D45%40AdobeOrg=-179204249%7CMCIDTS%7C17061%7CMCMID%7C51827214016119611801217576485496664924%7CMCAID%7CNONE%7CMCOPTOUT-1474115613s%7CNONE; _ga=GA1.2.927852513.1472530462; _gat_ea1bd6d040b5764fc83007c7c041712d=1; s_prevpage=Buy%20Lists%3Apage-1; s_nr=1474108414678-Repeat; s_cc=true; ui=mobile; trkid=49ccb94a-2623-4ecc-ab03-36844c034a42; ighs-sess=eyJhbmFseXRpY3NTZXNzaW9uSWQiOiI5NzkzZDk4NWFjZjdkOWFhODg2OTJhMTE4ZDc2MjE4MiJ9; ighs-sess.sig=PEsCCywXJi7yN6nFfxum-snE9Q4',
			'Host': 'shoponline.tescolotus.com', 'Referer': 'https://shoponline.tescolotus.com/groceries/th-TH/buy-lists/G00001097?buyListSourceId=G00001097&page=1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
			'x-csrf-token': 'SJ7aM8gU-Y8CtHMZ2TAK-bQXmvU40kJDwuKk', 'x-requested-with' : 'XMLHttpRequest'
}

x = 1
product = []
while x <= 30:	
	response = requests.get('https://shoponline.tescolotus.com/groceries/th-TH/shop/312/354/Cat00001738?page='+str(x)+'', headers=headers)
	data = response.json()


	i = 0
	while i < 24:

		q = []
		price = []

		try:
			q.append(data['productItems'][i]['product']['title'])
			q.append(data['productItems'][i]['product']['unitPrice'])
			q.append(data['productItems'][i]['product']['defaultImageUrl'])
			q.append('SCat0001738')
			q.append('Cat0001731')
			q.insert(0,'L'+str(((x-1)*24)+i+16489).zfill(6)+'')
			print (q, "\n")
		except:
			break

		product.append(q)

		i+=1
	if q == []:
		break

	x+=1

print(product)

csv_data_list = product
WriteToCSV(csv_file,csv_columns,csv_data_list)

#16527