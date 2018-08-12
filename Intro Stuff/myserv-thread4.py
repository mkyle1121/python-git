import socket
import threading
from SocketServer import ThreadingMixIn

class CLIENT(threading.Thread):

    def __init__(self, THREAD_OBJ, THREAD_IP, THREAD_PORT):
        threading.Thread.__init__(self)
        self.THREAD_OBJ = THREAD_OBJ
        self.THREAD_IP = THREAD_IP
        self.THREAD_PORT = THREAD_PORT
        print '[*] New Connection from',THREAD_IP,':',THREAD_PORT

    def run(self):
        while True:
            DATA = NEW_CLIENT_OBJ.recv(2048) #how is this ok?  crossing scopes...
            print DATA
            NEW_CLIENT_OBJ.send(DATA)

    # def SEND_DATA(self,SEND_DATA_OBJ):
    #     self.SEND_DATA_OBJ = SEND_DATA_OBJ
    #     while True:
    #         DATA = SEND_DATA_OBJ.recv(2048)  # how is this ok?  crossing scopes...
    #         print DATA
    #         SEND_DATA_OBJ.send(DATA)



SERVER_IP = '0.0.0.0'
TCP_PORT = 1234
SERVER_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SERVER_SOCKET.bind((SERVER_IP,TCP_PORT))
print '[*] Server listeninig on IP',SERVER_IP, 'and port',TCP_PORT
THREADS = []



while True:
    SERVER_SOCKET.listen(10)
    (NEW_CLIENT_OBJ, (NEW_CLIENT_IP, NEW_CLIENT_PORT)) = SERVER_SOCKET.accept()
    SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    NEW_CLIENT_THREAD = CLIENT(NEW_CLIENT_OBJ, NEW_CLIENT_IP, NEW_CLIENT_PORT)
    THREADS.append(NEW_CLIENT_THREAD)
    NEW_CLIENT_THREAD.start()
