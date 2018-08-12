


DICTION = {}

def ADD():
    KEY = raw_input('What key would you like to add? ')
    VALUE = raw_input('What value should this key have? ')
    DICTION [KEY] = VALUE
    VIEW()

def VIEW():
    for key in DICTION:
        print key,'=',DICTION[key]

def REM():
    VIEW()
    while True:
        REM_INPUT = raw_input('What key would you like to remove? ')
        if REM_INPUT in DICTION:
            del DICTION[REM_INPUT]
            break
            VIEW()
        else:
            print 'That is not in the list.'
            pass



while (True):
    print '''
    	1) Add an item to the list
    	2) Remove and item from the list
    	3) View the list
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

        #4) Insert an item at a specific location
        #5) Sort the list
        #6) Reverse the list
        #7) Search for an item

    # DIC = {'1': 'apples', '2': 'bananas'}
    #
    # print DIC
    #
    # while True:
    #
    #     a = raw_input('what would you like to delete? ')
    #
    #     if a in DIC:
    #         del DIC[a]
    #         break
    #     else:
    #         pass
    #
    # print DIC

