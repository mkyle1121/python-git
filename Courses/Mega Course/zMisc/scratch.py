'''some example for a doc'''

import datetime
import pandas

list1 = ['john', 'spot', 'sam']
list2 = ['apple', 'banana', 'jeans']

for a,b in zip(list1,list2):
    print (a)



with open('example.txt', 'a+') as F:
    F.write('\nsome text in here')

print(10000)

print (datetime.datetime.now())

l = lambda x: x**2

print (l(5))



with open('ALL_READ.txt', 'r+') as file:
    content = file.readlines()
    print (type(content),content)
    for item in content:
        print (item)

    file.seek(0)
    morecontent=file.read()
    print(morecontent)

class test:
    num=255
    def __init__(self):
        self.apple=250
test.num=88
person1 = test()
person2 = test()

#person1.num=177
person2.apple=399
#person2.num=188
#person1.num=person2.num
person1.apple=person2.apple

print (person1.num,person2.apple,person2.num,person1.apple,test.num)


df = pandas.DataFrame({'a':[4,5,6],'b':[7,8,9]},index=[1,2,3])
print('last line')

#df['new column']=df[10,11,12]

#df['c']=df[10,11,12]


print (df)
print (df.columns)
print (df.index)


df1=pandas.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['steak','juice','lemmon'],columns=['ham','bur','ger'])
print (df1)
print (df1.head(2))

df2=pandas.DataFrame({'A':'foo',
                      'B':['s','t','e','a','k',]},index=[1,2,3,4,5])

#df2['A']=df2['hambone']

print(df2.values)

print (df2)


df3=pandas.DataFrame({'Country': ['Belgium',  'India',  'Brazil'],'Capital': ['Brussels',  'New Delhi',  'Brasilia'],'Population': [11190846, 1303171035, 207847528]})
print(df3)
print(df3.iloc[1,1])

df3.iloc[1,1]='Pakistan'
print(df3)

print('BREAK-----------')

df3['Continent']=['Europe','Asia','South America']
print(df3)

df3=df3.rename(columns={'Capital':'Ham'})           #rename a column

print (df3)

print(df3['Population'])

import threading, time

def worker():
    print ('This is a thread')
    #time.sleep(3)
    print ('done sleeping')


t = threading.Thread(name='its working',target=worker)
#t.setDaemon(True)
t.start()
#time.sleep(1)
print('after thread')


class newclass:
    apple = []
    def __init__(self):
        self.apple.append('some data')

aaa = newclass()
bbb = newclass()

print (bbb.apple)







