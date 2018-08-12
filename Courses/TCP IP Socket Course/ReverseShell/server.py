import socket, sys




HOST = '0.0.0.0'
PORT = 9999

SOCKET = socket.socket()
SOCKET.bind((HOST, PORT))
SOCKET.listen(1)
CONN, ADDR = SOCKET.accept()
print("Connection from: ", ADDR)

while True:
    DATA = input('>>')
    if DATA == 'quit':
        CONN.close()
        SOCKET.close()
        sys.exit()
    if len(DATA.encode()) > 0:
        CONN.send(DATA.encode())
        client_response = str(CONN.recv(1024), 'utf-8')
        print(client_response, end='')

