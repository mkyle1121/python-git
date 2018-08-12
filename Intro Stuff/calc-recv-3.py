import Tkinter
import socket
import threading

class SERVER:
    def __init__(self, master):
        self.S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.S.bind(('127.0.0.1', 2222))
        self.S.listen(1)

        self.master = master
        master.title('Calc Recv')
        self.TEXT = Tkinter.Text(master, width=20, height=10)
        self.TEXT.pack(fill='both')

        self.T2 = threading.Thread(target=self.ACCEPT())
        self.T2.daemon = True
        self.T2.start()

    def ACCEPT(self):
        print 'Waiting to Accept...'
        self.TEXT.insert(1.0, 'Waiting to Accept\n')
        print 'After Insert'
        # self.CONN, self.ADDR = self.S.accept()
    #     print 'Accepted...'
    #     self.T1 = threading.Thread(target=self.RECV())
    #     self.T1.daemon = True
    #     self.T1.start()
    # def RECV(self):
    #     while True:
    #         print'Listening...'
    #         self.DATA = self.CONN.recv(1024)
    #         print 'The number is: ', self.DATA
    #         self.TEXT.insert(1.0, 'The number is:', self.DATA, '\n')


ROOT = Tkinter.Tk()
SERVER(ROOT)
ROOT.mainloop()