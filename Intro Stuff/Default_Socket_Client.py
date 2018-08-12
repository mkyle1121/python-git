import socket

HOST = '127.0.0.1'
PORT = 5000

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.connect((HOST, PORT))

MESSAGE = ''
while MESSAGE != 'q':
    MESSAGE = input('>>')
    SOCKET.send(MESSAGE.encode())
    #DATA = SOCKET.recv(1024)
    #print ('Received from server: ' + DATA.encode())

SOCKET.close()
