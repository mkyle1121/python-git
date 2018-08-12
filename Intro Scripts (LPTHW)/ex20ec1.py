from sys import argv

script, file = argv

OPEN = open(file, 'a+r+w')
print OPEN.name
print OPEN

#print "What would you like to add to the file?"
#ADD = raw_input()

print "Adding to the file..."
OPEN.write("I'm adding this.")

OPEN.seek(0)

print "All done, let's look at it."
print OPEN.read()

OPEN.close()

