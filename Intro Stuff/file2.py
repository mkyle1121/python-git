

NEWFILE = raw_input('What is the name of the new file? ')

FILE = open(NEWFILE,'w+')

WRITE_TEXT = raw_input('Please type what needs to be added: ')

FILE.write(WRITE_TEXT)

raw_input('Press enter to read the file.')

FILE.read()

FILE.close()

