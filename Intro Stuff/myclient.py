import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname('localhost')
PORT = 1234
IP_PORT = (IP, PORT)

SOCKET.connect((IP_PORT))
print 'Connected'

while True:
    # Grabbing unput
    MESSAGE = raw_input('What would you like to send (\'exit\' to quit): ')
    if MESSAGE == 'exit': #testing to exit
        print '[-]Goodbye'
        SOCKET.shutdown(0)
        SOCKET.close()
        break
    else:
        SOCKET.send(MESSAGE) #sending message
        print '[-]Message Sent'
        MESSAGE_RECV = SOCKET.recv(1024) #receiving ACK
        print '[-]Message Received'
        print MESSAGE_RECV