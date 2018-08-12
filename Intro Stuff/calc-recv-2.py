import socket
import Tkinter
import threading


class SERVER():
    def ACCEPT(self):
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.bind(('127.0.0.1', 2222))
        S.listen(1)
        print 'Waiting to Accept...'
        TEXT.insert(1.0, 'Waiting to Accept\n')
        print 'After Insert'
        self.CONN, self.ADDR = S.accept()
        print 'Accepted...'
        self.T1 = threading.Thread(target=self.RECV())
        self.T1.start()
    def RECV(self):
        # while True:
        print'Listening...'
        self.DATA = self.CONN.recv(1024)
        print 'The number is: ',  self.DATA
        TEXT.insert(1.0, 'The number is:', self.DATA, '\n')
            # if not self.DATA:
            #     break

LISTENER = SERVER()

T1 = threading.Thread(target=LISTENER.ACCEPT())
T1.start()



ROOT=Tkinter.Tk()
ROOT.geometry('250x200+1000+400')

TEXT = Tkinter.Text(ROOT, width=20, height=10)
TEXT.pack(fill='both')

# START_BUTTON = Tkinter.Button(ROOT, text='Start Server', bg='red', command=LISTENER.ACCEPT)
#START_BUTTON.pack(fill='both')

TEXT.insert(1.0, 'Ready...\n')

ROOT.mainloop()





