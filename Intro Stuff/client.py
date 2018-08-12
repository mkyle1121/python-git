
import socket
#
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ip=socket.gethostbyname('www.google.com')
# print ip
# port=80
#
# address=(ip,port)
# client.connect(address)
# print client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
#
# print client.recv(1024)


client = socket.socket()


client.connect(('127.0.0.1',1234))
client.send('Hello Server')

