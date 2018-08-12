

print "Enter the filename you wish to add: "
filename = raw_input(">> ")

print "Here is your output!"

txt=open(filename)
print txt.read()

print "I'll ask to make an addition."
add = raw_input()

print txt.read()

txt.close()