import socket, threading

class Server:

    def __init__(self):
        self.Remote_Conn_List = []
        self.Socket = socket.socket()
        self.Socket.bind(('', 1234))
        self.Socket.listen(5)
        print('Listening...')
        while True:
            print('Waiting to accept...')
            self.Remote_Conn_Obj, Remote_Addr_Tup = self.Socket.accept()
            self.Remote_Conn_List.append(self.Remote_Conn_Obj)
            print('Connection from ' + Remote_Addr_Tup[0] + ' ' + str(Remote_Addr_Tup[1]))
            print(self.Remote_Conn_List)
            Spawn_Accept_Thread = threading.Thread(target=self.accept())
            Spawn_Accept_Thread.setDaemon(True)
            Spawn_Accept_Thread.start()
    def accept(self):
        while True:
            if self.Remote_Conn_Obj:
                print('Waiting for data...')
                data = self.Remote_Conn_Obj.recv(1024)
                if not data:
                    self.Remote_Conn_Obj.close()
                    self.Remote_Conn_List.remove(self.Remote_Conn_Obj)
                    break
                else:
                    print (data.decode())

server = Server()



