
FILE = open('thisfile.txt', 'w+')

while True:
    print '1) Read the file'
    print '2) Write to the file'
    INPUT = raw_input('Type what you would like to do? ')

    if INPUT == '1':
        print FILE.read()
    elif INPUT == '2':
        WRITE = raw_input('Type the text here. ')
        if WRITE is None:
            pass
        else:
            FILE.write(WRITE)
    else:
        break

FILE.close()

