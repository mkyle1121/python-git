import random

deck = ['heart','spade','club','diamond']
numb = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']


for i in range(4):
    rand = random.randint(0,3)
    rand2 = random.randint(0,12)
    print numb[rand2],'of',deck[rand]
