def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b
	
print "Let's do some math with just functions"

age = add(30,5)
height = subtract(78,4)

print "age: %d, Height: %d" % (age, height)

print "Here is a puzzle."

what = add(age, subtract(height, 1))

print "That becomes: ",what, "Can you do it by hand?"

