#This is a game for Ellen to play
from sys import exit

def NAME():
	print "\n"
	NAME=raw_input("First things first, what is your name? ")
	print "\n"
	return NAME

def GOT(USER):
	

	print "Welcome",USER,"to the GAME OF THRONES!"
	print "You have immersed yourself in the 'Game of Thrones.'"
	print "Next to you is a valient steed and an archery range."
	print "What do you want to do?"
	print "\n"
	print "1)Get on the steed."
	print "2)Shoot some arrows."
	print "3)Leave the game."
	
	CHOICE=int(raw_input("> "))

	
	
	if CHOICE==1:
		print "You mount the steed."
		STEED()
	elif CHOICE==2:
		ARROW()
	elif CHOICE==3:
		FINISH()
	else:
		GOT()

def STEED():
	print "Where do you want to ride?"
	
	CHOICE=raw_input("> ")
	
	if "winterfell" in CHOICE:
		print "Winterfell?  What a great place to go this time of year!"
		print "YOU WIN!"
	elif "landing" in CHOICE:
		print "King's Landing?  They have to much money there and you die."
	elif "wall" in CHOICE:
		print "Damn that's a cold place, you die"
	else:
		print "That is not a place you can go."
		STEED()
		
def FINISH():
	print "Game Over!"

def ARROW():
	print "There are some arrows and targets next to you."
	print "What do you do?"
	print "\n"
	
	CHOICE=raw_input("> ")
	
	if "shoot" in CHOICE or "arrow" in CHOICE:
		print "You hit the bullseye!"
		print "Great shot!"
	else:
		print "Wrong move, someone came and shot you with an arrow."
		FINISH()
	
USER_NAME=NAME()
GOT(USER_NAME)