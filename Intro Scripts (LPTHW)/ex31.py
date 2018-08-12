print 'You enter a dark room with 3 doors.  Do you go through door 1 or door 2?'

door = raw_input('> ')

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Sit with the bear and eat cake" 
	
	bear = raw_input("> ")
	
	if bear == "1": 
		print "The bear eats your face off."
	elif bear == "2":
		print "The bear eats your legs off."
	elif bear == "3":
		print "What a nice meal."
	else:
		print "Well doing %s is probably better." % bear
	
elif door == "2":
	print "You stare into the endless abyss."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins"
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello."
	else:
		print "The insanity rots your eyes into a pool."
		
elif door == "3":
	print "There you get sucked into a blackhole and its amazing."
		

else:
	print "You stumble around and fall on a knife."