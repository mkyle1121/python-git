list = ['a','b','c']

for i,item in enumerate(list):
    print (str(i)+' '+item)

################################################
import socket,ssl
#
# HOST = '192.168.200.10'
# PORT = 22

#context = ssl.create_default_context()

#conn = context.wrap_socket(socket.socket(),server_hostname='www.google.com')

# hostname = socket.getfqdn('www.google.com')
#

# conn = socket.socket()
# conn.connect(('127.0.0.1', 5000))

# while True:
#
#     data = input ('>>')
#     if data == 'q': break
#     conn.sendall(str.encode(data))
#     recv_data = conn.recv(1024)
#     print (recv_data.decode())




# with open('some_data', 'rb+') as file:
#     print (file.name)
#     data = file.read()
#     print (data)
#     print (type(data))
#     conn.send(data)
#
# conn.shutdown(socket.SHUT_RDWR)
# conn.close()

a = lambda x,y: x * y

print (a(4,5))


def myfunc(list):
    prod_list=[]
    for x in range(10):
        for y in range(5):
            product = x*y
            prod_list.append(product)
    return prod_list + list

print (myfunc([100,101,102]))


b = lambda list: [x*y for x in range(10) for y in range(5)] + list

print (b([100,101,102]))


map()





