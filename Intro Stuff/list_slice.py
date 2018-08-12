import time

banana = [11,12,13,14,15,22,5,3,67]

print(banana[:])
print(banana[0:4])
print(banana[3:-1]) # up to last item, not include
print(banana[:6])
print(banana[5:2:-1]) # from 5 to 2 in reverse
print(banana[1:6:2])
#print(banana[9]) # out of range
print(banana[9:0:-1])
print(banana[-1:0:-1]) # print in reverse order, makes more sense
print(banana[::-1])

for i in range(100,90,-1): #starts at 100, ends at 91, different than END where last number is not used !!
    print (i)

for i in range(1,10,2):
    print (i)

apple = {'a':1,'b':2,'c':3}
for a in apple:
    print(apple[a])

print('loop time')

for i in banana:
    print(i)
    time.sleep(.5)
for i in banana[::-1]:
    print(i)
    time.sleep(.5)