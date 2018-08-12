from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print "Copying from ",fromfile,"to",tofile

input = open(fromfile)
indata = input.read()

print "The input file is",len(indata),"bytes long."

print "Does the output file exist? %r" % exists(tofile)

print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input()

output = open(tofile, 'w')
output.write(indata)

print "alright, all done."

output.close()
input.close()