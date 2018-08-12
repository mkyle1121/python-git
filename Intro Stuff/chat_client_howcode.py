import socket, threading, sys

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            data = raw_input('>>')
            if data == 'q':
                self.sock.shutdown(socket.SHUT_RDWR)
            else:
                self.sock.send(data)

    def __init__(self, address):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print data


if (len(sys.argv)) > 1:
    client = Client(sys.argv[1])
else:
    pass