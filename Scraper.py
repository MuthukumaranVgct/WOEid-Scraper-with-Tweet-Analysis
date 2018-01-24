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
	
	soup = BeautifulSoup(fetch(URL),'lxml')
	form = soup.findAll('form')
	#print(form[1])
	fields = form[0].findAll('input')

	formdata = dict( (field.get('name'), field.get('value')) for field in fields)

	formdata['place'] = city
	formdata['btn'] = 'submit'

	print('Place Name submitted. Wait for a while...\n')
	print('--------------------------------------------------------------------------------\n')
	posturl = u.urljoin(URL, form[0]['action'])

	r = s.post(posturl, data=formdata)

	'''file1 = open('file1.txt','w')
	file1.write(r.text)
	file1.close()'''

	temp = BeautifulSoup(r.text,'lxml')

	tablediv = temp.find('div', {'id':'lookup_result'})
	#print(temp)
	tablesoup = BeautifulSoup(str(tablediv),'lxml')
	table = tablesoup.find('table')
	#print(table)
	rows = table.findAll('tr')
	cols = rows[1].findAll('td')
	return(cols[3].find(text=True))
	
	    
