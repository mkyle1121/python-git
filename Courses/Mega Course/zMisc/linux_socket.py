import socket

Socket=socket.socket()
Socket.bind(('',1234))
Socket.listen(5)
print ('Listening...')
Remote_Connection_Obj, Remote_Address_Tupple=Socket.accept()

print ('Connected to: '+str(Remote_Address_Tupple[0])+' port '+str(Remote_Address_Tupple[1]))
print ('Sending...')
print (Socket)
print (type(Socket))
print (Remote_Connection_Obj)
print (type(Remote_Connection_Obj))


data=Remote_Connection_Obj.recv(150)
print('Printing data.')
#print (data.decode())
data=data.decode()
with open('random_file','w+') as file:
    file.write(data)
    file.seek(0)
    print(file.read())




