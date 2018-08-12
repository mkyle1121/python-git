import socket
import threading
from Tkinter import *


#
# class Server:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print 'Socket created..'
#     connections = []
#     def __init__(self):
#         print 'Started Listening'
#         self.sock.bind(('0.0.0.0', 10000))
#         self.sock.listen(1)
#         print 'Listeninig...'
#
#     def handler(self, c, a):
#         while True:
#             print 'Receiving...'
#             data = c.recv(1024)
#             print 'Waiting...'
#             for connection in self.connections:
#                 connection.send(data)
#                 print 'Sent Data to', connection
#             if not data:
#                 print (str(a[0]) + ':' + str(a[1]), 'disconnected')
#                 self.connections.remove(c)
#                 c.close()
#                 break
#
#     def run(self):
#         while True:
#             print 'Waiting to Accept...'
#             c, a = self.sock.accept()
#             print 'Connection Accepted by', a
#             cThread = threading.Thread(target=self.handler, args=(c, a))
#             cThread.daemon = True
#             cThread.start()
#             print 'Thread started'
#             self.connections.append(c)
#             print(self.connections)
#             print (str(a[0]) + ':' + str(a[1]), 'connected')
#









sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendMsg(data):
    while True:
     #   data = raw_input('>>')
        if data == 'q':
            sock.shutdown(socket.SHUT_RDWR)
        else:
            sock.send(data)

def recvMsg(address):
    sock.connect((address, 10000))
    print 'connected'

    # iThread = threading.Thread(target=sendMsg(send_entry.get()))
    # iThread.daemon = True
    # iThread.start()

    while True:
        print ' about to send data in loop'
        data = sock.recv(1024)
        if not data:
            break
        else:
            print'in else look for data'
            main_box.insert(data)
            print data


############GUI

root = Tk()

root.title('Muaike Chats')
#
# server_button = Button(root, text='Act as Server', bg='gray', width=13, height=2)
# server_button.grid(row=0, column=0, rowspan=2, sticky=W)

address_label = Label(root, anchor=E, width=14, text='IP Address:')
address_label.grid(row=0, column=1)
#address_label.config(borderwidth=1, relief='solid')




address_entry = Entry(root, width=16)
address_entry.grid(row=0, column=2, sticky=E)

connect_button = Button(root, text='CONNECT', bg='green', width=13, command=(lambda: recvMsg(address_entry.get())))
connect_button.grid(row=1, column=2, sticky=E)



main_box = Text(root, width=40, height=15)
main_box.grid(row=2, columnspan=3)

send_entry = Entry(root, width=35)
send_entry.grid(row=3, columnspan=2)

send_button = Button(root, text='Send', bg='green', width=9, command=(lambda: sendMsg(send_entry.get())))
send_button.grid(row=3, column=2, sticky=W)

quit_button = Button(root, text='Quit', bg='red', command=root.quit)
quit_button.grid(row=3, column=2, sticky=E)





#
# client = Client(sys.argv[1])
#
# server = Server()
# server.run()
#


root.mainloop()
#
