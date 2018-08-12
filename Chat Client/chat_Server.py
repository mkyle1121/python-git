import socket, threading

class ClientThread(threading.Thread):
    ClientList = []

    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        self.ClientList.append(clientsocket)
        print ("[+] New thread started for "+ip+":"+str(port))

    def run(self):
        print ("Connection from : "+ip+":"+str(port))

        while True:
            try:
                data = self.csocket.recv(1000000)
                if not data:
                    print("Client at " + ip + ' ' + str(port) + " disconnected...")
                    for remote_client in self.ClientList:
                        if remote_client == self.csocket:
                            pass
                        else:
                            remote_client.send('[*]A user has disconnected.\n'.encode())
                    self.ClientList.remove(self.csocket)
                    self.csocket.close()
                    break
                else:
                    #print ("Client(%s:%s) sent :  \n%s"%(self.ip, str(self.port), data.decode()))
                    for remote_client in self.ClientList:
                        if remote_client == self.csocket:
                            pass
                        else:
                            remote_client.send(data)
            except ConnectionResetError:
                print ('Connection Reset by Peer. '+self.ip+' '+str(self.port))
                for remote_client in self.ClientList:
                    if remote_client == self.csocket:
                        self.ClientList.remove(self.csocket)
                break

host = "0.0.0.0"
port = 1234

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((host,port))

while True:
    tcpsock.listen(4)
    print ("Listening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()

    #pass clientsock to the ClientThread thread object being created
    newthread = ClientThread(ip, port, clientsock)
    newthread.daemon = True
    newthread.start()