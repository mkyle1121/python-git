__author__ = 'mike'

import requests
from bs4 import BeautifulSoup

#request = requests.get('http://www.google.com')
#print (request)
#print(request.content)



#request = requests.get('http://www.johnlewis.com/john-lewis-wade-office-chair-black/p447855')

request = requests.get('https://www.johnlewis.com/bosch-zamo-digital-laser/p3194404')
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {'class':'price price--large'}) # in the 'p' tag with attributes 'class'.
#can find any tag and any attribute to get the text inside of it. 'p' or 'div' or whatever.


#element = str(element.text).replace(' ','',200) # remove white space
string_price = str(element.text).strip() # remove all whitespace and newlines
#element = str(element).replace('\n','',100) # remove new lines
price_wo_symbol = string_price[1:]


print ('k', end='stank'); print (repr(price_wo_symbol),end=''); print ('k') # repr is raw string
print (float(price_wo_symbol))

print ('The price of the chair is {}'.format(price_wo_symbol))
#<span itemprop='price' class='now-price'> 115.00 </span>
