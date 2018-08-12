



while True:


    while True:
        try:
            X = int(raw_input('Please input the 1st number: '))
            break
        except ValueError:
            print 'Please input a number.'

    while True:
        try:
            Y = int(raw_input('Please input the 2nd number: '))
            break
        except ValueError:
            print 'Please input a number.'



    print '''        
    1) Add
    2) Subtract
    3) Multiply
    4) Divide
    '''

    while True:
        try:
            Z = int(raw_input('What operation would you like to do: '))   #loop for integer number between 1 and 4
            if Z <= 4 and Z >= 1 :
                break
        except:
            print 'Please input a number between 1 and 4'


    SUM = 0

    if Z == 1:
        SUM = X + Y
    elif Z == 2:
        SUM = X - Y
    elif Z == 3:
        SUM = X * Y
    elif Z == 4:
        SUM = X / Y
    else:
        pass

    print 'The answer is: ', SUM, '\n'




