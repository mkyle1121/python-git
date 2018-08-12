import ssl,socket

#context = ssl.create_default_context()
context =ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode=ssl.CERT_NONE
#context.check_hostname = True
#context.load_verify_locations('/etc/ssl/certs/ca-bundle.crt')
hostname = socket.getfqdn('www.google.com')

conn = context.wrap_socket(socket.socket())
conn.connect((hostname, 443))

while True:

	data = input ('>>')
	if data == 'q': break
	conn.sendall(str.encode(data))

conn.shutdown(socket.SHUT_RDWR)
conn.close()