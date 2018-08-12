import socket

host = '127.0.0.1'
port = 0

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = ('127.0.0.1', 5000)


alias = raw_input('Name: ')
message = raw_input(alias + ">>")

while message != 'q':
    if message != '':
        s.sendto(alias + ':' + message, server)
        message = raw_input(alias + '>>')
        data, addr = s.recvfrom(1024)

s.close()
