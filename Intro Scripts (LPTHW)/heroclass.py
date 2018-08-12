class Hero:
	'''
	A hero who is allergic to apples
	'''
	def __init__(self,name):
		self.name = name
		self.health = 100
	def eat(self,food):
		if (food == 'apple'):
			self.health -= 100
		elif (food == 'ham'):
			self.health += 20
Bob = Hero('Bob')
print Bob.name
print Bob.health
Bob.eat('ham')
print Bob.health
