import random
import os
import time

class PLAYER:
    def __init__(self):
        self.PLAYER_DECK = []
        self.name = ''
        self.PLAYER_CARD_STORE = ''
        for i in range(4):
            x = random.choice(DECK)
            DECK.remove(x)
            self.PLAYER_DECK.append(x)
    def SEE_CARD_METHOD(self, SEE_CARD_PLAYER1):
        if SEE_CARD_PLAYER1 == 1:
            print '[%s] [X] [X] [X]' %self.PLAYER_DECK[0]
        elif SEE_CARD_PLAYER1 == 2:
            print '[X] [%s] [X] [X]' %self.PLAYER_DECK[1]
        elif SEE_CARD_PLAYER1 == 3:
            print '[X] [X] [%s] [X]' %self.PLAYER_DECK[2]
        elif SEE_CARD_PLAYER1 == 4:
            print '[X] [X] [X] [%s]' %self.PLAYER_DECK[3]
        else:
            pass
        raw_input('\nPress Enter when ready. ')
    def TAKE(self):
        global DECK_CARD
        print 'You chose to take, what card would you like to replace? (Number 1 - 4)'

        while True:
            try:
                TAKE_CHOICE = int(raw_input('>> '))
                if TAKE_CHOICE >= 1 and TAKE_CHOICE <= 4:
                    break
                else:
                    print 'That is not between 1 and 4'
            except:
                print 'Please enter a number.'
        try:
            DECK.remove(DECK_CARD)      #remove the deck card sent to player from the deck
        except:
            pass
        try:
            DECK.remove[self.PLAYER_DECK[TAKE_CHOICE-1]]        #remove from deck the player's card
        except:
            pass
        self.PLAYER_CARD_STORE = self.PLAYER_DECK[TAKE_CHOICE - 1]  # store the player card
        self.PLAYER_DECK[TAKE_CHOICE - 1] = DECK_CARD  # set player card to deck card
        DECK_CARD = self.PLAYER_CARD_STORE      #set deck card from player stored card
        print 'You gave up the [%s]' %DECK_CARD
        raw_input('Press Enter. ')
        os.system('cls')
        self.SEE_CARD_METHOD(TAKE_CHOICE)       #print new deck for player
    def DRAW(self):
        global DECK_CARD
        DRAW_CARD_CHOICE = random.choice(DECK)      #setting draw choice
        os.system('cls')
        print '[X]]] [%s] [%s]<--Drawn Card \n' % (DECK_CARD, DRAW_CARD_CHOICE)

        print '[X] [X] [X] [X]\n'

        print '''What would you like to do?
1) Keep the card.
2) Set the card on the deck.'''
        while True:
            try:
                DRAW_CHOICE = int(raw_input('>> '))
                if DRAW_CHOICE >= 1 and DRAW_CHOICE <= 2:
                    break
                else:
                    print 'That is not between 1 and 2'
            except:
                print 'Please enter a number.'
        if DRAW_CHOICE == 1:
            ####replace a card
            print 'Which card would you like to replace? (Number between 1 - 4)'
            while True:
                try:
                    DRAW_CHOICE_REPLACE = int(raw_input('>> '))
                    if DRAW_CHOICE_REPLACE >= 1 and DRAW_CHOICE_REPLACE <= 4:
                        break
                    else:
                        print 'That is not between 1 and 4'
                except:
                    print 'Please enter a number.'

            if DRAW_CHOICE_REPLACE == 1:

                self.PLAYER_DECK.insert(0, DRAW_CARD_CHOICE)        #set player card 1 to drawn card
                try:
                    DECK.remove(self.PLAYER_DECK[1])        #test if replaced card can be removed in main deck
                except:
                    pass        #if it is already gone just pass
                                # DECK REMOVE IS AT BOTTOM
                DECK_CARD = self.PLAYER_DECK.pop(1)     #set the deck card to the player card that was replaced (popped)
                print 'You gave up the [%s]' %DECK_CARD
                raw_input('Press Enter. ')
                self.SEE_CARD_METHOD(DRAW_CHOICE_REPLACE)       #show the card chosen
            elif DRAW_CHOICE_REPLACE == 2:
                self.PLAYER_DECK.insert(1, DRAW_CARD_CHOICE)
                try:
                    DECK.remove(self.PLAYER_DECK[2])
                except:
                    pass
                DECK_CARD = self.PLAYER_DECK.pop(2)
                print 'You gave up the [%s]' %DECK_CARD
                raw_input('Press Enter. ')
                self.SEE_CARD_METHOD(DRAW_CHOICE_REPLACE)
            elif DRAW_CHOICE_REPLACE == 3:
                self.PLAYER_DECK.insert(2, DRAW_CARD_CHOICE)
                try:
                    DECK.remove(self.PLAYER_DECK[3])
                except:
                    pass
                DECK_CARD = self.PLAYER_DECK.pop(3)
                print 'You gave up the [%s]' %DECK_CARD
                raw_input('Press Enter. ')
                self.SEE_CARD_METHOD(DRAW_CHOICE_REPLACE)
            elif DRAW_CHOICE_REPLACE == 4:
                self.PLAYER_DECK.insert(3, DRAW_CARD_CHOICE)
                try:
                    DECK.remove(self.PLAYER_DECK[4])
                except:
                    pass
                DECK_CARD = self.PLAYER_DECK.pop(4)
                print 'You gave up the [%s]' %DECK_CARD
                raw_input('Press Enter. ')
                self.SEE_CARD_METHOD(DRAW_CHOICE_REPLACE)
        elif DRAW_CHOICE == 2:
            try:
                DECK.remove(DECK_CARD)
            except:
                pass
            ####set the card on the deck
            DECK_CARD = DRAW_CARD_CHOICE

        try:
            DECK.remove(DRAW_CARD_CHOICE)  # remove drawn card from the deck which is in players deck
        except:
            pass
    def KNOCK(self):
        pass
    def REMOVE_DECK(self,NUM):
        global DECK_CARD
        try:
            DECK.remove(DECK_CARD)  # try to remove deck card
        except:
            pass
        try:
            DECK.remove(COMP.PLAYER_DECK[NUM])  # try to remove the deck card
        except:
            pass
        self.PLAYER_CARD_STORE = COMP.PLAYER_DECK[NUM]  # set store card from temp comp deck
        COMP.PLAYER_DECK[NUM] = DECK_CARD  # set temp comp deck from deck card
        DECK_CARD = self.PLAYER_CARD_STORE  # set deck card from temp comp store card
        print 'Computer took the [%s] and left the [%s]' %(COMP.PLAYER_DECK[NUM], DECK_CARD)
        raw_input('Press Enter.')
    def REMOVE_DRAW(self,NUM):
        global DECK_CARD
        global COMP_DRAW_CARD
        try:
            DECK.remove(COMP_DRAW_CARD)
        except:
            pass
        try:
            DECK.remove(COMP.PLAYER_DECK[NUM])
        except:
            pass

        self.PLAYER_CARD_STORE = COMP.PLAYER_DECK[NUM]
        COMP.PLAYER_DECK[NUM] = COMP_DRAW_CARD
        DECK_CARD = self.PLAYER_CARD_STORE

        print 'Computer drew the [%s] and left the [%s]' % (COMP.PLAYER_DECK[NUM], DECK_CARD)
        raw_input('Press Enter. ')

####################  setting variables #####################################

DECK = []
SUITS = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
VALUES = {}
COMP_DRAW_CARD = ''
COMP_VALUE_KNOCK = random.randint(5, 12)
COMP_TOTAL = 0
RUNNING = True


###########################computer logic#####################

def COMPUTER_TURN():
    global COMP_VALUE_KNOCK
    global DECK_CARD
    global COMP_DRAW_CARD
    global COMP_TOTAL
    global RUNNING

    os.system('cls')
    print 'Computer turn...'
    time.sleep(2)

    while True:
        if VALUES[DECK_CARD] < VALUES[COMP.PLAYER_DECK[0]]:
            COMP.REMOVE_DECK(0)
            break
        elif VALUES[DECK_CARD] < VALUES[COMP.PLAYER_DECK[1]]:
            COMP.REMOVE_DECK(1)
            break
        elif VALUES[DECK_CARD] < VALUES[COMP.PLAYER_DECK[2]]:
            COMP.REMOVE_DECK(2)
            break
        elif VALUES[DECK_CARD] < VALUES[COMP.PLAYER_DECK[3]]:
            COMP.REMOVE_DECK(3)
            break
        else:
            COMP_DRAW_CARD = random.choice(DECK)
            if VALUES[COMP_DRAW_CARD] < VALUES[COMP.PLAYER_DECK[0]]:
                COMP.REMOVE_DRAW(0)
                break
            elif VALUES[COMP_DRAW_CARD] < VALUES[COMP.PLAYER_DECK[1]]:
                COMP.REMOVE_DRAW(1)
                break
            elif VALUES[COMP_DRAW_CARD] < VALUES[COMP.PLAYER_DECK[2]]:
                COMP.REMOVE_DRAW(2)
                break
            elif VALUES[COMP_DRAW_CARD] < VALUES[COMP.PLAYER_DECK[3]]:
                COMP.REMOVE_DRAW(3)
                break
            else:
                try:
                    DECK.remove(COMP_DRAW_CARD)
                except:
                    pass
                DECK_CARD = COMP_DRAW_CARD
                print 'Computer drew the [%s] and left the [%s]' %(COMP_DRAW_CARD, DECK_CARD)
                raw_input('Press Enter. ')
                break

    COMP_TOTAL = 0
    for SUM in range(4):
        COMP_TOTAL += VALUES[COMP.PLAYER_DECK[SUM]]

    if COMP_TOTAL <= COMP_VALUE_KNOCK:
        print 'The computer knocks!'
        print 'Player gets one last chance.'
        time.sleep(2)
        RUNNING = False


def FINISH():
    os.system('cls')
    PLAYER1_TOTAL = 0
    COMP_TOTAL = 0

    for SUM in range(4):
        PLAYER1_TOTAL += VALUES[PLAYER1.PLAYER_DECK[SUM]]
        COMP_TOTAL += VALUES[COMP.PLAYER_DECK[SUM]]

    print 'Your DECK value is %i:' %PLAYER1_TOTAL
    print PLAYER1.PLAYER_DECK
    print '\n'
    print 'The Computer DECK is %i:' %COMP_TOTAL
    print COMP.PLAYER_DECK
    print '\n'

    if PLAYER1_TOTAL < COMP_TOTAL:
        print 'You are the Winner %s!' %PLAYER1.name
    elif COMP_TOTAL < PLAYER1_TOTAL:
        print 'The Computer won this time %s!' %PLAYER1.name
    elif PLAYER1_TOTAL == COMP_TOTAL:
        print 'It is a tie!'

    print 'The computer threshold was %i:' %COMP_VALUE_KNOCK


######### POPULATE THE DECK ############

for i in SUITS:
    x = 'King of %s' %i
    DECK.append(x)
    VALUES[x] = 0

for i in SUITS:
    x = 'Ace of %s' %i
    DECK.append(x)
    VALUES[x] = 1

for i in range(2, 11):
    for j in SUITS:
        x = '%s of %s' %(i,j)
        DECK.append(x)
        VALUES[x] = i

for i in SUITS:
    x = 'Jack of %s' %i
    DECK.append(x)
    VALUES[x] = 10

for i in SUITS:
    x = 'Queen of %s' %i
    DECK.append(x)
    VALUES[x] = 10

####################creating player objects#########################

PLAYER1 = PLAYER()
COMP = PLAYER()

################## Main Script ################################

os.system('cls')
print '''Hello and welcome to GOLF!  It is you versus the computer.
First, what is your name?'''
PLAYER1.name = raw_input('>> ')
print 'Welcome %s, let us begin.' %PLAYER1.name
raw_input('Press Enter. ')
os.system('cls')
print 'Here are 4 cards face down, pick the first card you want to see (Number 1 - 4).\n'
print '[X] [X] [X] [X]'

while True:
    try:
        SEE_CARD = int(raw_input('>> '))
        if SEE_CARD >= 1 and SEE_CARD <= 4:
            break
        else:
            print 'That is not between 1 and 4'
    except:
        print 'Please enter a number.'

os.system('cls')
PLAYER1.SEE_CARD_METHOD(SEE_CARD)
os.system('cls')

print 'Pick the second card you want to see (Number 1 - 4).\n'
print '[X] [X] [X] [X]'

while True:
    try:
        SEE_CARD = int(raw_input('>> '))
        if SEE_CARD >= 1 and SEE_CARD <= 4:
            break
        else:
            print 'That is not between 1 and 4'
    except:
        print 'Please enter a number.'

os.system('cls')
PLAYER1.SEE_CARD_METHOD(SEE_CARD)
os.system('cls')

################## BEGIN PLAY ########################

DECK_CARD = random.choice(DECK)
DECK_CARD_STORE = ''

while True:

    os.system('cls')

    print '[X]]] [%s] \n' %DECK_CARD

    print '[X] [X] [X] [X]\n'

    print '''What would you like to do?
1) TAKE the card shown.
2) DRAW a new card from the deck.
3) KNOCK.'''

    CHOICE = 0
    while True:
        try:
            CHOICE = int(raw_input('>> '))
            if CHOICE >=1 and CHOICE <=3:
                break
            else:
                print 'Please pick 1, 2, or 3.'
        except:
            print 'Please pick a number.'

    if CHOICE == 1:
        PLAYER1.TAKE()
        if RUNNING == False:
            FINISH()
            break
        COMPUTER_TURN()
    elif CHOICE == 2:
        PLAYER1.DRAW()
        if RUNNING == False:
            FINISH()
            break
        COMPUTER_TURN()
    elif CHOICE == 3 and RUNNING == True:
        print 'Computer goes one last time...'
        time.sleep(1)
        COMPUTER_TURN()
        FINISH()
        break

print 'Thanks for playing!'





