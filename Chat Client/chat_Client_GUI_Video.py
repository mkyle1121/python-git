import socket, threading, pickle, cv2, time
from tkinter import *
from datetime import datetime as dt

###################### Threading for Recv ################################

class ClientThread(threading.Thread):
    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
	
    def run(self):          # for receive of data
        #old_data_length=0
        img_size = '0'
        data = b''
        img_size_set = False
        while True:
            try:
                packet = self.csocket.recv(2000000)
                print ('Length of packet is: '+str(len(packet)))
                if len(packet) <= 1024:
                    decoded_packet = packet.decode()
                    if decoded_packet == 'quit_video':
                        cv2.destroyAllWindows()
                        packet = b''
                    elif decoded_packet[0:9] == 'img_size:':
                        img_size = decoded_packet[9:]
                        print('set img size to: ' +img_size)
                        img_size_set = True
                        packet = b''
                    else:
                        app.recv(packet.decode())
                        packet = b''
                data += packet
                print ('data size: '+str(len(data)))
                if len(data) == int(img_size) and img_size_set == True:
                    f1 = pickle.loads(data)
                    data = b''
                    packet = b''
                    cv2.imshow('Received Video', f1)
                    cv2.waitKey(1)
                if len(data) >= 2000000:
                    data = b''
            except OSError:
                print ('Connection Closed Recv')
                break

###################### Threading for Video ###############################3

class ClientThreadVideo(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket

    def run(self):                  #for sending video
        img_size_sent = False
        video = cv2.VideoCapture(0)
        while True:
            ret, frame = video.read()
            f1 = pickle.dumps(frame)
            img_size = len(f1)
            if img_size_sent == False:
                self.csocket.send('img_size:'.encode()+str(img_size).encode())
                print ('sent img size of: '+str(img_size))
                img_size_sent = True
                time.sleep(.2)
            self.csocket.send(f1)
            cv2.imshow('Sending Video', frame)
            if cv2.waitKey(1) == ord('q'):
                time.sleep(.2) #allow quit to be sent after rest of frame data
                self.csocket.send('quit_video'.encode())
                break
        cv2.destroyAllWindows()
        video.release()

######################## GUI Construction ##################################

class chat:
    def __init__(self, window):

        #### TCP Socket Construction ####
        #self.host = '13.57.125.9'
        self.host = '192.168.200.1'
        #self.host = 'localhost'
        self.port = 1234
        self.name = '<No Name Set>'

        ############# Main Chat Window Construction ########

        self.window = window
        self.window.bind('<Return>',self.send_data)
        self.window.title('Muaike Chat')

        self.t1=Text(self.window, width=65, height=20, bd=7, highlightcolor='red',
                     wrap=WORD, cursor='arrow', padx=2, background='white smoke', font=('arial', 10))
        self.t1.grid(row=0,column=0,columnspan=3)
        self.t1.insert(END, '[*] Welcome to Muaike Chat.\n[*] 1) Go to Connect and set the server.\n[*] 2) Go to Connect and click Connect\n[*] 3) Set your Name in the Edit menu\n')
        self.sb1 = Scrollbar(window, command=self.t1.yview)
        self.sb1.grid(row=0, column=3, sticky=NS)
        self.t1['yscrollcommand'] = self.sb1.set
        self.t1.config(state='disabled')

        self.send_text = StringVar()
        self.e1 = Entry(self.window, textvariable=self.send_text, bd=3, cursor='arrow',
                        highlightcolor='red', highlightthickness=2)
        self.e1.grid(row=2, column=1, sticky=EW, columnspan=2)

        self.b6 = Button(self.window, text='Video', bg='cyan', width=8, borderwidth=3,
                         command=self.send_video)
        self.b6.grid(row=3, column=0)

        self.b1 = Button(self.window, text='Send', bg='light green', width=8, borderwidth=3,
                         command=self.send_data)
        self.b1.grid(row=3, column=2, sticky=E)

        self.set_name = StringVar()
        self.l1 = Label(self.window, borderwidth=3, relief='raised',
                        background='tomato', textvariable=self.set_name)
        self.l1.grid(row=2, column=0, sticky=EW)
        
        ############ MENUBAR #####################
        menubar = Menu(self.window, borderwidth=2)
        filemenu = Menu(menubar)
        editmenu = Menu(menubar)
        connectmenu = Menu(menubar)
        menubar.add_cascade(label='File', menu=filemenu, background='dark gray')
        filemenu.add_command(label='Exit', command=self.destroy)
        menubar.add_cascade(label='Edit', menu=editmenu, background='dark gray')
        editmenu.add_command(label='Name...', command=self.edit_name)
        menubar.add_cascade(label='Connect', menu=connectmenu, background='dark gray')
        connectmenu.add_command(label='Connect', command=self.connect)
        connectmenu.add_command(label='Close', command=self.close)
        connectmenu.add_command(label='Server...', command=self.connect_server)
        self.window.config(menu=menubar)

        ############ Top level Construction ##################

##################### GUI Methods ########################################

    def send_data(self, event=None):
        self.data_to_send = str('('+dt.now().strftime('%I:%M:%S')+') '+self.name+': '+self.send_text.get()+'\n')
        try:
            self.tcpsock.send(self.data_to_send.encode())
            self.t1.config(state='normal')
            self.t1.insert(END, self.data_to_send,'RED')
            self.t1.tag_config('RED', foreground='red')
            self.t1.see(END)
            self.t1.config(state='disabled')
            self.e1.delete(0, END)
        except OSError:
            self.t1.config(state='normal')
            self.t1.insert(END, '[*]Server Not Connected\n')
            self.t1.see(END)
            self.t1.config(state='disabled')
        except AttributeError:
            self.t1.config(state='normal')
            self.t1.insert(END, '[*]Server Not Connected\n')
            self.t1.see(END)
            self.t1.config(state='disabled')

    def connect(self):
        try:
            self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcpsock.connect((self.host,self.port))
            self.t1.config(state='normal')
            self.t1.insert(END,'[*]Connected to Server: '+self.host+':'+str(self.port)+'\n')
            self.t1.see(END)
            self.t1.config(state='disabled')
            self.newthread = ClientThread(self.host,self.port,self.tcpsock)
            self.newthread.daemon = True
            self.newthread.start()
        except OSError:
            self.t1.config(state='normal')
            self.t1.insert(END, '[*]Server Cannot Connect.  Already Connected?\n')
            self.t1.see(END)
            self.t1.config(state='disabled')

    def recv(self,data):
        self.t1.config(state='normal')
        self.t1.insert(END,data)
        self.t1.see(END)
        self.t1.config(state='disabled')

    def name_ok(self,event=None):
        self.name = self.get_name.get().upper()
        self.top.destroy()
        self.set_name.set(self.name+' :')

    def destroy(self):
        try:
            self.tcpsock.shutdown(socket.SHUT_RDWR)
            self.tcpsock.close()
        except OSError:
            pass
        except AttributeError:
            pass
        self.window.destroy()

    def edit_name(self):
        self.top = Toplevel()
        self.top.geometry('180x150+100+100')
        self.top.attributes('-topmost', 'True')
        self.top.bind('<Return>', self.name_ok)
        ############ Labels, Entry, Button ###################
        self.l2 = Label(self.top, text='Enter Your Name First:')
        self.l2.grid(row=0, column=0, padx=30, pady=10)
        self.get_name = StringVar()
        self.e2 = Entry(self.top, bd=3, justify=CENTER, textvariable=self.get_name)
        self.e2.grid(row=1, column=0, padx=30, pady=10)
        self.b4 = Button(self.top, text='OK', bd=2, command=self.name_ok)
        self.b4.grid(row=2, column=0, padx=40)

    def connect_server(self):
        self.top2 = Toplevel()
        self.top2.geometry('180x150+100+100')
        self.top2.attributes('-topmost', 'True')
        self.top2.bind('<Return>', self.set_host)
        ############ Labels, Entry, Button ###################
        self.l3 = Label(self.top2, text='Enter Server IP:')
        self.l3.grid(row=0, column=0, padx=30, pady=10)
        self.get_server_IP = StringVar()
        self.e3 = Entry(self.top2, bd=3, justify=CENTER, textvariable=self.get_server_IP)
        self.e3.grid(row=1, column=0, padx=30, pady=10)
        self.b5 = Button(self.top2, text='OK', bd=2, command=self.set_host)
        self.b5.grid(row=2, column=0, padx=40)

    def set_host(self, event=None):
        self.host = self.get_server_IP.get()
        self.t1.config(state='normal')
        self.t1.insert(END, '[*]Server Set To: '+self.host+'\n')
        self.t1.see(END)
        self.t1.config(state='disabled')
        self.top2.destroy()

    def close(self):
        try:
            self.tcpsock.shutdown(socket.SHUT_RDWR)
            self.tcpsock.close()
            self.t1.config(state='normal')
            self.t1.insert(END, '[*]Connection To Server Closed.\n')
            self.t1.see(END)
            self.t1.config(state='disabled')
        except OSError:
            self.t1.config(state='normal')
            self.t1.insert(END, '[*]Server Not Connected.\n')
            self.t1.see(END)
            self.t1.config(state='disabled')

    def send_video(self):
        self.newthread_video = ClientThreadVideo(self.host, self.port, self.tcpsock)
        self.newthread_video.daemon = True
        self.newthread_video.start()

######################### MAINLOOP ######################################

window=Tk()
app=chat(window)
window.mainloop()