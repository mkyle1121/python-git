import codecs
import tkinter
import socket

def INPUT_FUNC(VAR):
    INPUT.delete(0, 'end')
    INPUT.insert(0, VAR)
    LIST.append(VAR)
    print (LIST)

def MATH_FUNC(VAR):
    global MATH
    if VAR == 1:
        MATH=1
    elif VAR == 2:
        MATH=2
    elif VAR == 3:
        MATH=3
    elif VAR == 4:
        MATH=4
    else:
        pass

def EQ_FUNC():
    global MATH
    global SUM
    if MATH==1:
        SUM = LIST[0] + LIST[1]
    elif MATH==2:
        SUM = LIST[0] - LIST[1]
    elif MATH==3:
        SUM = LIST[0] * LIST[1]
    elif MATH==4:
        SUM = LIST[0] / LIST[1]
    else:
        pass
    print ('SUM is', SUM)
    INPUT.delete(0, 'end')
    INPUT.insert(0, SUM)
    LIST[:] = []

def CL_FUNC():
    INPUT.delete(0, 'end')
    LIST[:] = []

class CONNECT():
    global SUM
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        pass
    def CONN(self):
        self.S.connect(('127.0.0.1', 2222))
        print ('Connection Established')
    def RUN(self):
        self.S.send(codecs.encode(str(SUM)))
        print ('Sent', SUM)
    def CLOSE(self,event):
        self.S.close()
        print ('Connection Closed')


#######################################################

ROOT = tkinter.Tk()
ROOT.title('Muaike\'s Calc')
ROOT.geometry('200x200+800+400')
LIST = []
MATH=0
SUM=0
SOCKET = CONNECT()

INPUT = tkinter.Entry(ROOT, width=31)
INPUT.grid(row=0, columnspan=4, padx=5, pady=5)

BUTTON_1 = tkinter.Button(ROOT, text = '1', width=5, command=lambda: INPUT_FUNC(1))
BUTTON_1.grid(row=1, column=0)

BUTTON_2 = tkinter.Button(ROOT, text = '2', width=5, command=lambda: INPUT_FUNC(2))
BUTTON_2.grid(row=1, column=1)

BUTTON_3 = tkinter.Button(ROOT, text = '3', width=5, command=lambda: INPUT_FUNC(3))
BUTTON_3.grid(row=1, column=2)

BUTTON_4 = tkinter.Button(ROOT, text = '4', width=5, command=lambda: INPUT_FUNC(4))
BUTTON_4.grid(row=2, column=0)

BUTTON_5 = tkinter.Button(ROOT, text = '5', width=5, command=lambda: INPUT_FUNC(5))
BUTTON_5.grid(row=2, column=1)

BUTTON_6 = tkinter.Button(ROOT, text = '6', width=5, command=lambda: INPUT_FUNC(6))
BUTTON_6.grid(row=2, column=2)

BUTTON_7 = tkinter.Button(ROOT, text = '7', width=5, command=lambda: INPUT_FUNC(7))
BUTTON_7.grid(row=3, column=0)

BUTTON_8 = tkinter.Button(ROOT, text = '8', width=5, command=lambda: INPUT_FUNC(8))
BUTTON_8.grid(row=3, column=1)

BUTTON_9 = tkinter.Button(ROOT, text = '9', width=5, command=lambda: INPUT_FUNC(9))
BUTTON_9.grid(row=3, column=2)

BUTTON_0 = tkinter.Button(ROOT, text = '0', width=5, command=lambda: INPUT_FUNC(0))
BUTTON_0.grid(row=4, column=1)

############################

BUTTON_ADD = tkinter.Button(ROOT, text = '+', width=5, command=lambda: MATH_FUNC(1))
BUTTON_ADD.grid(row=1, column=3)

BUTTON_SUB = tkinter.Button(ROOT, text = '-', width=5, command=lambda: MATH_FUNC(2))
BUTTON_SUB.grid(row=2, column=3)

BUTTON_MUL = tkinter.Button(ROOT, text = '*', width=5, command=lambda: MATH_FUNC(3))
BUTTON_MUL.grid(row=3, column=3)

BUTTON_DIV = tkinter.Button(ROOT, text = '/', width=5, command=lambda: MATH_FUNC(4))
BUTTON_DIV.grid(row=4, column=3)

################################

BUTTON_EQ = tkinter.Button(ROOT, text = '=', width=5, bg='green', command=lambda: EQ_FUNC())
BUTTON_EQ.grid(row=4, column=2)

BUTTON_CL = tkinter.Button(ROOT, text = 'C', width=5, bg='red', command=lambda: CL_FUNC())
BUTTON_CL.grid(row=4, column=0)

################################

BUTTON_CONN = tkinter.Button(ROOT, text = 'Conn', width=5, bg='lightblue', command=SOCKET.CONN)
BUTTON_CONN.grid(row=5, column=0)
BUTTON_CONN.bind('<Button-3>', SOCKET.CLOSE)

BUTTON_SEND = tkinter.Button(ROOT, text = 'SEND', width=19, bg='lightblue', command=SOCKET.RUN)
BUTTON_SEND.grid(row=5, column=1, columnspan=3)







ROOT.mainloop()