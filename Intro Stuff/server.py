import socket


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = socket.gethostbyname('localhost')
port = 1234
address = (ip,port)

server.bind(address)
server.listen(10)
print '[*] Started listeninig on',ip,'.',port
client,addr=server.accept()
print '[*] Got a connection from',addr[0],'.',addr[1]

while True:
    data = client.recv(1024)
    print '[*] Recieved',data,'from the client'
    print '    Processing data'
    if(data=='Hello Server'):
        client.send("Hello Client")
        print 'Processing done \n'
    elif(data=='disconnect'):
        client.send("Goodbye")
        client.close()
        break
    else:
        client.send('Data was not valid')
        print 'Processing done - Invalid data \n'

