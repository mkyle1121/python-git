import random


HIGH = 10
answer = random.randrange(HIGH)
guess=raw_input("Guess a number from 0 to %d: " %HIGH)

while (int(guess) != answer):
    if (int (guess) < answer):
        print 'it is higher.'
    else:
        print 'answer is lower'
    guess=raw_input("Guess a number from 0 to %d: " %HIGH)

raw_input("You are a winner!")
        
        
