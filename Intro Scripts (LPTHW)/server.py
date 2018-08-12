# server.py

import socket

port = 1111
s = socket.socket()
host = socket.gethostname()
s.bind((host,port))
s.listen(5)

print 'Server linstening...'

while True:
	conn, addr = s.accept()
	print 'Got connection from', addr
	data = conn.recv(1024)
	print('Server recieved', repr(data))
	
	filename='to.txt'
	f = open(filename,'rb')
	l = f.read(1024)
	while (1):
		conn.send(1) 
		print('Sent ',repr(1))
		l = f.read(1024)
	f.close()
	
	print('Done sending')
	conn.send('Thank you for connecting')
	conn.close()
	
	