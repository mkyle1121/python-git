import numpy
import cv2


n = numpy.arange(30)

print (n)

n=n.reshape(5,6)

print (n)

im_g=cv2.imread('grey1.png',0)

#print (im_g)

print (im_g[0])
print (im_g[1])

print(len(im_g[0])+len(im_g))

row0 = im_g[0]
print ('row 0 from list')
print (row0[20:31])

CAR = cv2.imread('car.png',0)

print (CAR)
print (len(CAR))
print (len(CAR[0]))
print (CAR[0])

print (CAR[0,1]) # print row (list) 0, item number 1


COLOR = cv2.imread('color_circle.jpg',1)
print (COLOR)
print ('break line')
#print (COLOR[0])
print (len(COLOR))
# print (len(COLOR))
#
# print (type(COLOR))
#
# for i in COLOR:
#     print (i)
#     break

print (COLOR[0,1])  # = 153 153 153   --- these are the BGR values!!!!!
#### each block in the array is a row
#### the number of items in the array is the length across (number of columns)
##its just like grayscale except each item has 3 items for BGR


# print ('BREAK--------------------------------------------')
# SMALL = cv2.imread('small_color_circle.jpg',1)
# print (SMALL)

