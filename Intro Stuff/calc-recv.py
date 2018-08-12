import socket
import tkinter
import threading
import codecs


class SERVER():
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        self.S.bind(('127.0.0.1', 2222))
        self.S.listen(1)
    def START(self):
        self.T10 = threading.Thread(target=self.ACCEPT())
        self.T10.daemon = True
        self.T10.start()
    def ACCEPT(self):

        print ('Waiting to Accept...')
        TEXT.insert(1.0, 'Waiting to Accept\n')
        print ('After Insert')
        self.CONN, self.ADDR = self.S.accept()
        print ('Accepted...')
        self.T1 = threading.Thread(target=self.RECV())
        self.T1.daemon = True
        self.T1.start()
    def RECV(self):
        while True:
            print ('Listening...')
            self.DATA = self.CONN.recv(1024)
            RECV_DATA = codecs.decode(self.DATA)
            print (RECV_DATA)
            print ('The number is: ', RECV_DATA)
            TEXT.insert(1.0, 'The number is:', RECV_DATA, '\n')
            if not self.DATA:
                break

LISTENER = SERVER()

ROOT=tkinter.Tk()
ROOT.geometry('250x200+1000+400')

TEXT = tkinter.Text(ROOT, width=20, height=10)
TEXT.pack(fill='both')

START_BUTTON = tkinter.Button(ROOT, text='Start Server', bg='red', command=LISTENER.START)
START_BUTTON.pack(fill='both')

TEXT.insert(1.0, 'Something\n')

ROOT.mainloop()







