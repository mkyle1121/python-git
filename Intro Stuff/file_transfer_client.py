import socket
import codecs
import os

def recv_data():
    print('Waiting to Receive.')
    recv = connection.recv(10000)
    recv = codecs.decode(recv)
    return recv

connection=socket.create_connection(('127.0.0.1',5000))
print ('Connected.')

data = recv_data()

with open('ZZZZ TEXT','w+') as file:
    file.write(data)
    file.seek(0)
    print(file.read())

print(recv_data())



