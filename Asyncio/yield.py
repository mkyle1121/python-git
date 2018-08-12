import time
import datetime

# somelist = [x-10 for x in range(10)]
#
# print(somelist)
#
# genlist = (x-10 for x in range(10))
# # generator is like list but can only be used once to save memory
# for i in genlist:
#     print(i)
# print(genlist)
# # generator can only be used once
# print('here')
# for i in genlist:
#     print(i)

print(datetime.datetime.now())
print (time.time())

genlist = []

def gen():
    for i in range(10):
        yield i



print(genlist)
print('here now')
gener = gen() # create generator from yield in gen()

print (gener)
for i in gener:
    print(i)

print ('one mo gain')
# second time will not work
for i in gener:
   print(i)