#client.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 1111

s.connect((host,port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
	print 'file opened'
	while True:
		print('recieving data...')
		data = s.recv(1024)
		print('data=%s', (data))
		if not data:
			break
			f.write(data)
			
f.close()
print('Successfully get the file')
s.close()
print('connection closed')
