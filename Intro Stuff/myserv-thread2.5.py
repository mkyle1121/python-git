import socket
import threading



def CLIENT_1(CLIENT_OBJ):
    while True:
        MESSAGE = CLIENT_OBJ.recv(1024)  # Receive client data
        print '[-]Message Received'
        if MESSAGE == 'close':
            CLIENT_OBJ.close()
            SOCKET.shutdown(socket.SHUT_RD)
            SOCKET.close()
            print '[-]Client closed connection'
            break
        else:
            print MESSAGE
            CLIENT_OBJ.send()  # sending ACK
            return MESSAGE



# def CLIENT_2():
#     CLIENT_OBJ, ADDR = SOCKET.accept()  # accepting connections
#     print '[-]Connected with', ADDR[0], 'at', ADDR[1]  # client IP and PORT
#
#     while True:
#         MESSAGE = CLIENT_OBJ.recv(1024)  # Receive client data
#         print '[-]Message Received'
#         print MESSAGE
#
#         SEND_MESSAGE = '[-]OK!'
#         CLIENT_OBJ.send(SEND_MESSAGE)  # sending ACK
#         print '[-]Reply Sent'
#


#socket creation, binding, listening
SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket creation
IP = '0.0.0.0' #listen on all ports
PORT = 1234 #TCP port
IP_PORT = (IP,PORT) #create tuple
SOCKET.bind(IP_PORT) #binding the IP and PORT
print '[-]Socket bound...'
SOCKET.listen(10) #listeninig
print '[-]Listening...'

CLIENT_MESSAGE=''

while True:
    CLIENT_OBJ, ADDR = SOCKET.accept()  # accepting connections
    print '[-]Connected with', ADDR[0], 'at', ADDR[1]  # client IP and PORT
    #starting client 1 thread
    threading._start_new_thread(CLIENT_1,(CLIENT_OBJ,))

CLIENT_OBJ.close()
SOCKET.close()

#
# #starting client2 thread
# T2 = threading.Thread(target=CLIENT_2)
# T2.start()




