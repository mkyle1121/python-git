import socket
import threading
from multiprocessing.pool import ThreadPool

#function for accepting connections
def ACCEPT():
    OBJ, ADDR = SOCKET.accept()  # accepting connections
    print '[-]Connected with', ADDR[0], 'at', ADDR[1]  # client IP and PORT
    return OBJ

#socket creation, binding, listening
SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket creation
IP = '0.0.0.0' #listen on all ports
PORT = 1234 #TCP port
IP_PORT = (IP,PORT) #create tuple
SOCKET.bind(IP_PORT) #binding the IP and PORT
print '[-]Socket bound...'
SOCKET.listen(10) #listeninig
print '[-]Listening...'

# T1 = threading.Thread(target=ACCEPT)
# T1.start()

#Threadpool for accepting connections
pool = ThreadPool(processes=1)
ASYNC_RESULT = pool.apply_async(ACCEPT)
CLIENT_OBJ = ASYNC_RESULT.get()

while True:
    MESSAGE = CLIENT_OBJ.recv(1024)  # Receive client data
    print '[-]Message Received'
    print MESSAGE

    SEND_MESSAGE = '[-]OK!'
    CLIENT_OBJ.send(SEND_MESSAGE)  # sending ACK
    print '[-]Reply Sent'

