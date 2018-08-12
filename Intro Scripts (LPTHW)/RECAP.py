#from sys import argv
#script, qw, er, ty = argv
from os.path import exists



print "Something here."
# this is a comment
print 'something else.'
print "another 'quote'"

print "Animals are", 30+40, "count."
print "what is",7,"letters"
print 5>6
print 7+13

beds = 13
chairs = 7
print beds+chairs

name = "mike"
othername = "steve"
num=70
print "my name is %s %s, and i am %d" %(name,othername,num)

num=10
num2=20
num3=30
print "these are the numbers %s %d %d" % ("This",num2,num3)
print num+num2+num3
str="something "
ing="fresh"
print str+ing
a="apples"
print "i have %s" % a

print "..." *  10

print "hi \nthis \nis \nnew"
plant="daisy, tulip, lavendar"
print "Here are the plants", plant

print "this is \t tabbed in"
print "this is a backslash \\"

print "Pick a number"
#num10=raw_input()
#print "You picked",num10

#ab=raw_input("Say something...")
#print ab

#print "you entered", qw + er + ty

#file = raw_input("What is your filename? ")
#print "Does the file exist?", exists(file)
#aa = open(file)
#print aa.read()

'''
print "Whats the filename?"
fn = raw_input()
fileobject = open(fn, "r+")
print "Here is the contents..."
print fileobject.read()
print fileobject.truncate()
print "Here is the file again"
print fileobject.read()
line = raw_input("Add a line:")
fileobject.write(line)
print "Here is the file after the line"
print fileobject.read()
fileobject.close()
'''

def P1(x):
	print "You typed",x
#func = raw_input("Type something ")
#P1(func)

def calc(x,y,z):
	a=x+y+z
	print "Your total is", a
#print "Enter 3 numbers:"
#a=int(raw_input())
#b=int(raw_input())
#c=int(raw_input())
#calc(a,b,c)

def TWO(A):
	UNO=A*5
	DOS=A*10
	return UNO,DOS
BAKED,BEANS=TWO(5)
print "UNO is",BAKED
print "DOS is",BEANS

TANK=int(raw_input("Enter a number>"))
if TANK>5:
	print "It is greater than 5"
elif TANK<5:
	print "It is less than 5"
else:
	print "It is not a number"
	
LIST=["bed","sheets","pillows"]
for ITEM in LIST:
	print ITEM

def gold_room():
	print "This room is full of gold.  How much do you take?"
	
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)	
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
	
	
#gold_room()


def silver_room():
	print "The room is full of silver, how much do you take?"
	take = int(raw_input("> "))
	if take < 50:
		print "You are very kind."
	else:
		print "Greedy!"
	
silver_room()