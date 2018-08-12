people=20
cats=30
dogs=15

if people < cats:
	print "Too many cats."
	
if people > cats:
	print "Not many cats"
	
dogs += 5

if people >= dogs:
	print "People are greater than equal to dogs."
	
people=30
cars=30
buses=15

if cars>people:
	print "We should take the cars."
elif cars<people:
	print "We should not take the cars."
else:
	print "We cannot decide."