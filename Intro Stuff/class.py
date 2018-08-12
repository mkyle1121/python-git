class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return emp_1.first + ' ' + emp_1.last


emp_1 = Employee('Corey', 'Schafer')
emp_2 = Employee('Test', 'User')

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

#print emp_1.fullname





class className:
    def createName(self, name):
        self.name = name
    def displayName(self):
        return self.name
    def saying(self):
        print 'hello %s' % self.name

print className()
first = className()
second = className()

first.createName('bucky')
second.createName('Tony')

print first.displayName()
first.saying()

print first.name






class DOOR:
    def __init__(self, wood, color, feet):
        self.wood = wood
        self.color = color
        self.feet = feet
    def INFO(self):
        print 'The door is made from',self.wood,'is the color',self.color,'and is',self.feet,'feet tall.'
    def UPDATE(self,newsize):
        self.feet = newsize

ROOMDOOR = DOOR('mahogany','pink','6')
ROOMDOOR.UPDATE('5')
ROOMDOOR.INFO()

#######class copying .... sublass and superclass

class parentClass:
    var1='i am var1'
    var2='i am var2'

class childClass(parentClass):
    pass



parent = parentClass
print parent.var1

child = childClass
print child.var2




class parent:
    var1='bacon'
    var2='snausage'

class child(parent):
    var2='toast'


child1 = child

print child1.var2













