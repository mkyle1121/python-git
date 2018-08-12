import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.google.com/')
print (r)
print (r.text)
print ('--------------------------------------')
print (r.headers)
print ('--------------------------------------t')

c = r.content
print (c)
print ('******************************************')
soup = BeautifulSoup(c,'html.parser')
print (soup)
print ('#####################################')
all = BeautifulSoup.prettify(soup)
print (all)