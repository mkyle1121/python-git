from sys import argv

script, file = argv


fo = open(file, 'r+w')
print fo
print fo.name

#print "Which line would you like to read?" 
#x=int(raw_input())
	
#line=fo.readline()

#print line


#print list(fo)

fo.write("something")

#print fo.read()

print fo.readline()
print fo.readline()
print fo.readline()

fo.close() 