import socket

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

# while True:
s.listen(1)
c, addr = s.accept()
print "Connection from: ", addr
while True:
    print 'send time'
    data = c.recv(1024)
    if not data:
        break
    print "from connected user: " + data
     # data = str(data).upper()
     # print "sending: " + data
     # c.send(data)
     # c.close()

