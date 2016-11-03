import urllib.request
import re

#i = 1
#while i<=5:

#	htmlfile = urllib.request.urlopen("https://shoponline.tescolotus.com/groceries/th-TH/buy-lists/G00001097?buyListSourceId=G00001097&page="+str(i)+"")

#	htmltext = htmlfile.read().decode('utf-8')


#	regex = '([0-9]{1,4}\.[0-9][0-9])</span></span></div></div></div></div><!--'

#	pattern = re.compile(regex)

#	price = re.findall(pattern,htmltext)

#	print (price)
#	i+=1
headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'en-US,en;q=0.8'
			,'Cache-Control':'max-age=0','Connection':'keep-alive','Cookie':'splashpage_confirm=splashpage; _ga=GA1.3.1731975964.1472531847; frontend=bej8jsj6ujmo7kslk0ao33lea2',
			'Host':'www.bigc.co.th','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

pagefile = urllib.request.urlopen('http://www.bigc.co.th/food.html?limit=100', headers=headers)

htmltext = pagefile.read().decode('utf-8')

regex = '<span class="price">฿([0-9]{1,4}\.[0-9][0-9])</span>'  

pattern = re.compile(regex)

price = re.findall(pattern,htmltext)

print(price, "\n")