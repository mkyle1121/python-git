import sys


LIST=[]

def ADD():
	ADD_INPUT = raw_input('Type what you would like to add. ')
	LIST.append(ADD_INPUT)
	VIEW()
def REM():
	VIEW()
	REM_INPUT = int(input("Which item number would you like to remove? "))
	LIST.pop(REM_INPUT)
	VIEW()
def VIEW():
	NUM = 0
	print '\n'
	for i in LIST:
		print NUM,i 
		NUM+=1
def INSERT():
	INSERT_INPUT_NAME = raw_input("What would you like to insert? ")
	INSERT_INPUT_ITEM = int(input("What item number would you like to insert it to? "))
	LIST.insert(INSERT_INPUT_ITEM,INSERT_INPUT_NAME)
	VIEW()
def SORT():
	LIST.sort()
	VIEW()
def REV():
	LIST.reverse()
def SEARCH():
	SEARCH_INPUT = raw_input('What would you like to search for? ')
	SEARCH_ITEM = LIST.index(SEARCH_INPUT)
	print '\n That is item number',SEARCH_ITEM	

INPUT = 0
	
while (True):
	print '''
	1) Add an item to the list
	2) Remove and item from the list
	3) View the list
	4) Insert an item at a specific location
	5) Sort the list
	6) Reverse the list
	7) Search for an item
	8) Exit
	'''
	
	INPUT = raw_input("What would you like to do? ")
		
	if (INPUT == '1'):
		ADD()
	elif (INPUT == '2'):
		REM()
	elif (INPUT == '3'):
		VIEW()
	elif (INPUT == '4'):
		INSERT()
	elif (INPUT == '5'):
		SORT()
	elif (INPUT == '6'):
		REV()
	elif (INPUT == '7'):
		SEARCH()
	elif (INPUT == '8'):
		print "QUITTING!"
		break
	else:
		pass