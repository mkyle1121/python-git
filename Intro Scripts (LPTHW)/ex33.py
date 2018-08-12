def WHILE(i,B,C):
	numbers=[]

	while i<=B:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i=i+C
		#print "Numbers now: ", numbers
		#print "At the bottom i is %d" % i 
		
	return numbers
	
	
START=int(raw_input("What number would you like to start with? "))
END=int(raw_input("What number would you like to end with? "))
INC=int(raw_input("What number would you like to increment by? "))

COUNT=WHILE(START,END,INC)	
	
print "The numbers: "

for num in COUNT:
	print num 
	