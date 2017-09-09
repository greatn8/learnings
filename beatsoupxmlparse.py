from bs4 import BeautifulSoup
import urllib2


data = urllib2.urlopen('https://abr.business.gov.au/abrxmlsearch/AbrXmlSearch.asmx/SearchByRegistrationEvent?postcode=&state=&entityTypeCode=&month=8&year=2017&authenticationGuid=62301559-37d7-4505-8a1d-1c429ff09e63').read()

print data
print type(data)

soup = BeautifulSoup(data, 'xml')
print type(soup)

for abn in soup.find_all('abn'):
	print(abn.text)


#
#