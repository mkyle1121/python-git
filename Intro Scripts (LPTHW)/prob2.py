
x=0
y=1
z=0
a=0

while(z<4000000):
	z=x+y
	print x,'+',y,'=',z 
	x=y
	y=z
	
	if (z%2==0):
		a=a+z
		print 'a =',a
	else:
		pass




