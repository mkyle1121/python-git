import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created...'
    connections = []
    def __init__(self):
        print 'Started Listening'
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)
        print 'Listeninig...'

    def handler(self, c, a):
        while True:
            print 'Receiving...'
            data = c.recv(1024)
            print 'Waiting...'
            for connection in self.connections:
                connection.send(data)
                print 'Sent Data to', connection
            if not data:
                print (str(a[0]) + ':' + str(a[1]), 'disconnected')
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            print 'Waiting to Accept...'
            c, a = self.sock.accept()
            print 'Connection Accepted by', a
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            print 'Thread started'
            self.connections.append(c)
            print(self.connections)
            print (str(a[0]) + ':' + str(a[1]), 'connected')






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
    server = Server()
    server.run()




