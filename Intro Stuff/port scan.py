import socket
import sys
import io

port = int(sys.argv[2])


SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    SOCKET.connect((sys.argv[1], port))
    result = 'success'
    print result
except:
    result = 'error'
    print result
    pass

FILE = io.open('ZZ TEXT', 'a+', encoding='utf8')
print FILE.readable()
print 'write time'
FILE.write(unicode(result+'\n'))
FILE.read(80)

SOCKET.send(FILE.read())

SOCKET.close()