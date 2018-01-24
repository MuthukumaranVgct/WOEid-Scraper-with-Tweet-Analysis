from bs4 import BeautifulSoup
import requests
import urllib.parse as u
s = requests.Session()
def fetch(url, data=None):
	if data is None:
		return s.get(url).content
	else:
		return s.post(url, data=data).content
def Scraping():
	city=input("Enter a City Name or Country Or a State Name")
	URL = 'http://woeid.rosselliot.co.nz/'
	
#put your code here
