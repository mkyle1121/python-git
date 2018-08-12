import os


class MAIN_FILE():

    def MENU(self):
        MENU_INPUT=''
        while True:
            print '''What would you like to do?
    
                   1) List files in directory
                   2) Create a new file
                   3) Add to an existing file
                   4) Read an existing file
                   5) Quit
                   '''
            while True:
                try:
                    MENU_INPUT = int(raw_input('Selection: '))
                    if MENU_INPUT <= 5 and MENU_INPUT >= 1:
                        break
                    print 'Please input a number between 1 and 5'
                except:
                    print 'Please input a number between 1 and 5'

            if MENU_INPUT == 1:
                self.LIST()
            elif MENU_INPUT == 2:
                self.CREATE()
            elif MENU_INPUT == 3:
                self.ADD()
            elif MENU_INPUT == 4:
                self.READ()
            elif MENU_INPUT == 5:
                print 'Finished'
                break
            else:
                pass

    def LIST(self):
        LIST = []
        LIST = os.listdir('C:/Users/Mike Kyle/PycharmProjects/pythonstuff/')
        for i in LIST:
            print i

    def CREATE(self):
        USER_FILE = raw_input('What is the file name? ')
        OPEN_FILE = open(USER_FILE, 'w')
        print 'Created file', USER_FILE
        OPEN_FILE.close()

    def ADD(self):
        while True:
            USER_FILE = raw_input('What is the file name? (quit to exit) ')
            if USER_FILE == 'quit':
                break
            OPEN_FILE = open(USER_FILE, 'a+')
            print 'Opened', USER_FILE
            break
        while True:
            USER_ADD = raw_input('Type what to add (quit to exit): ')
            if USER_ADD == 'quit':
                OPEN_FILE.close()
                break
            OPEN_FILE.write(USER_ADD)
            OPEN_FILE.write('\n')
            OPEN_FILE.read()

    def READ(self):
        while True:
            USER_FILE = raw_input('What is the file name? (quit to exit) ')
            if USER_FILE == 'quit':
                break
            OPEN_FILE = open(USER_FILE, 'r')
            print 'Opened', USER_FILE
            OPEN_FILE.read()
            OPEN_FILE.close()


USER = MAIN_FILE()

USER.MENU()

