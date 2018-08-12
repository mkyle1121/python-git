hairs = ['brown','blonde','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for loop goes through a list

for number in the_count:
	print "This is count %d" % number
	
for fruit in fruits:
	print "a fruit of type: %s" % fruit
	
for i in change:
	print "I got %r" % i
	
elements = []

for i in range(0, 6):
	print "adding %d to the list." % i
	elements.append(i)
	
for i in elements:
	print "Element was: %d" % i
	
	
up = [1,8,5,3,6,]
	
for a in up:
	print "This is the number: ",a