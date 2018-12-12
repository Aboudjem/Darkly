import urllib2
from bs4 import BeautifulSoup
import sys

ip = "192.168.1.34"
content_list = []

def main(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, features="html.parser")
	links = soup.find_all('a')
	for link in links:
		href = link.get('href')
		if href == "README" :
			tmp = urllib2.urlopen(url + '/' + href )
			content = str(tmp.read().strip())
			if content not in content_list:
				print(str(url) + "=>" + content)
				content_list.append(content)	
		elif href != "../":
			main(url + href)

if __name__ == "__main__":
	url = 'http://' + ip + '/.hidden/'
	main(url)