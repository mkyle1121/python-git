x=0
xx=0
while (x < 1000):
	x+=3
	if (x>=1000):
		break
	else:	
		xx+=x
		print 'X is',x
		print 'XX is',xx

raw_input("Ready for Y")
	
y=0
yy=0
while(y < 1000):
	y+=5
	if (y>=1000):
		break
	else:
		yy=yy+y
		print 'Y is',y
		print 'YY is',yy
		
	
raw_input("Add together")

print 'y is',y
print 'x is',x
print 'yy is',yy
print 'xx is',xx


z=xx+yy

print "XX + YY =",z