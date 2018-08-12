import socket

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
data = ''


while True:
    if data == 'q':
        break
    data, addr = s.recvfrom(1024)
    print data
    s.sendto(data,addr)

s.close()
