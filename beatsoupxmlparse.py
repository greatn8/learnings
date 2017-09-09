#getting abn registered in a month and year & learning git

from bs4 import BeautifulSoup
import urllib2



data = urllib2.urlopen('https://abr.business.gov.au/abrxmlsearch/AbrXmlSearch.asmx/SearchByRegistrationEvent?postcode=&state=&entityTypeCode=&month=8&year=2017&authenticationGuid=62301559-37d7-4505-8a1d-1c429ff09e63').read()

#print data for testing
print data
#print type for testing
print type(data)

#makine string into soup and speicify its xml
soup = BeautifulSoup(data, 'xml')
print type(soup)

#for each abn in xm document print abn
for abn in soup.find_all('abn'):
	print(abn.text)


#function for getting details of each abn
def getabndetails(abninstance):
	abnindividual = str(abninstance)
	abnsearch = urllib2.urlopen('https://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/SearchByABNv201408?searchString=' + abnindividual + '&includeHistoricalDetails=N&authenticationGuid=62301559-37d7-4505-8a1d-1c429ff09e63').read()
	#print for testing
	print abnsearch
	#print type for testing
	print type(abnsearch)

	#makine string into soup and speicify its xml
	soup1ABN = BeautifulSoup(abnsearch, 'xml')
	
	#print type of souop
	print "soup type",type(soup1ABN)
	#testing geting one piece of info from returend company info, added limit 1 to avoid trading name
	companyname = soup1ABN.find_all('organisationName', limit=1)
	#Making sure its in a tring
	print 'company name type', type(companyname)
	print "Company name:",companyname


#testing function with one ABN
getabndetails(74172177893)