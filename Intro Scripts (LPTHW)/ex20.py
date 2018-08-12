from sys import argv

script, inputfile = argv

def printall(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def printaline(linecount, f):
	print linecount, f.readline()
	
currentfile = open(inputfile)

print "First lets print the whole file:\n"

printall(currentfile)

print "Now let's rewind, kind of like a tape."

rewind(currentfile)

print "Let's print three lines:"

currentline = 1
printaline(currentline, currentfile)

currentline = currentline + 1
printaline(currentline, currentfile)

currentline = currentline + 1
printaline(currentline, currentfile)