import telnetlib
import time
import threading

username = 'teopy'
password = 'python\r\n'
HOST = '192.168.200.101'
READ_TIMEOUT = 5



# def recv():
#       while True:
#               print ('start recv')
#               c = connection.read_some()
#               print (str(c,'utf-8'), end='')


connection = telnetlib.Telnet(HOST)

a = connection.read_until(b'name:', READ_TIMEOUT)
print (str(a,'utf-8'), end='')

input_name = input()

connection.write(input_name.encode()+'\n'.encode())
#connection.write(username.encode())

b = connection.read_until(b'word:', READ_TIMEOUT)
print (str(b,'utf-8'), end='')

input_pass = input()

connection.write(input_pass.encode()+'\n'.encode())
# c_input=''

# t1 = threading.Thread(target=recv())
# t1.daemon = True
# t1.start()

# print ('Input')

# while c_input != 'exit':
#       print ('start input')

#       c = connection.read_very_eager()
#       print (str(c,'utf-8'), end='')
#       c_input = input()
#       connection.write(c_input.encode()+'\n'.encode())

#connection.write('terminal length 0\n'.encode())
time.sleep(1)
connection.write('configure terminal\n'.encode())
time.sleep(1)

with open('cmd_file','r') as file:
        r = file.readlines()
        for line in r:
                connection.write(line.encode()+'\n'.encode())
                time.sleep(1)


connection.close()