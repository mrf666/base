from bs4 import BeautifulSoup
import requests

user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://www.google.com/",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"}


url = "https://www.minimaks.ru/about/vendors/"

names = list()
place = list()
phones = list()
emails = list()
'''
page = BeautifulSoup(requests.get(url, headers = user_agent).text,"lxml")
print(page.span)
for name in page.find_all("div", class_ = "text-block-vendor"):
	name_text = name.text
	print(name_text)
'''

page = requests.get(url)

if page.status_code ==200:
	soup = BeautifulSoup(page.text, "html.parser")
	print("hello")
	allNews = soup.findAll('div', class_='vendor-manager')
	for data in allNews:
		if data.find("span", class_ = "name") is not None:
			names.append(data.text)
		if data.find("a") is not None:
			emails.append(data.text)

	for data in names:
		print(data)
	for data in emails:
		print(data)


"""
if page.status_code == 200:
	print("ok")

	soup = BeautifulSoup(page.text,"lxml")
	allLinks = soup.findAll('div', class_ = 'text-block-vendor')
	#print(allLinks.get_text)
	#b = allLinks.findAll('div',class_='text-block-vendor')
	for data in allLinks:
				if data.find('span') is not None:
					names.append(data.text)

				print(names)
"""