from sys import argv

script, file = argv

print "Please input a the text you would like to add: "
data = raw_input()

openfile = open(file, 'w')
openfile.write(data)
openfile.write("\n")

openfile.close()

