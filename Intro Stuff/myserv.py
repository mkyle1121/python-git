import socket

SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket creation

IP = '0.0.0.0' #listen on all ports
PORT = 1234 #TCP port

IP_PORT = (IP,PORT) #create tuple
SOCKET.bind(IP_PORT) #binding the IP and PORT
print '[-]Socket bound...'

SOCKET.listen(10) #listeninig
print '[-]Listening...'

CLIENT_OBJ, CLIENT_ADDR = SOCKET.accept()  # accepting connections
# print '[-]Connected client object',CLIENT_OBJ #client object
print '[-]Connected with', CLIENT_ADDR[0], 'at', CLIENT_ADDR[1]  # client IP and PORT

while True:

    MESSAGE = CLIENT_OBJ.recv(1024) #Receive client data
    print '[-]Message Received'
    print MESSAGE

    SEND_MESSAGE = '[-]OK!'
    CLIENT_OBJ.send(SEND_MESSAGE) #sending ACK
    print '[-]Reply Sent'

