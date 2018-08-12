import socket
import os
import codecs

sock=socket.socket()
sock.bind(('127.0.0.1',5000))
sock.listen()

def send_data(send):
    connection.send(codecs.encode(send))

def accept():
    print('Listening...')
    connection, remote_address = sock.accept()
    print('Connection from:', connection)
    print('Connected address:', remote_address)
    return connection

def list_to_str():
    list_directory_str = ''
    list_directory = os.listdir()
    for item in list_directory:
        list_directory_str = list_directory_str + item + '\n'
    return list_directory_str

connection = accept()

with open('ZZ TEXT','r') as file:
    data=file.read()
    print(data)

send_data(data)

send_data(list_to_str())





