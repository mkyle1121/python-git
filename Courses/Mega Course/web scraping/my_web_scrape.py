from bs4 import BeautifulSoup
import requests
import pandas

base_url = 'http://www.zumiez.com/skate/skateboard-decks.html'

r=requests.get(base_url)
c=r.content
#print(c)
soup=BeautifulSoup(c,'html.parser')
#all=BeautifulSoup.prettify(soup)
#print(all)
all=soup.find_all('div',{'class':'product-name'})
#print (all)

l=[]
for item in all:
    l.append(item.text.replace('\n','').replace('  ',''))

#for i in l:
#    print(i)

df = pandas.DataFrame({'Skateboard Decks':l})

print (df.loc[5:10])

print (df)

df.to_csv('skb.csv')