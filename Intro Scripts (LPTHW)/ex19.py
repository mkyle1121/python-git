def candc(cheese,crackers):
	print "You have %d cheeses!" % cheese
	print "You have %d boxes of crackers" % crackers
	print "Man that's enough for a party."
	print "Get a blanket! \n"
	
print "We can just give the function numbers directly:"
candc(20, 30)

print "OR, we can use variables from our script.:"
cheese = 10
crackers = 50

candc(cheese,crackers)

print "we can even do math inside too:"
candc(10+20,5+6)

print "and we can combine the 2, variables and math"
candc(cheese+100,crackers+1000)
