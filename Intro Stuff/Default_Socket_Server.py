import socket

HOST = '127.0.0.1'
PORT = 5000

SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SOCKET.bind((HOST, PORT))



while True:
    SOCKET.listen(1)
    CONN, ADDR = SOCKET.accept()
    print("Connection from: ", ADDR)
    DATA = CONN.recv(1024)
    if not DATA:
        CONN.close()
        break
    print ("from connected user: " + DATA.decode())
    #CONN.send(DATA)


