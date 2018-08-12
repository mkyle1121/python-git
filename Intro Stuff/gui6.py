from Tkinter import *


class MikeButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printbutton = Button(frame, text='print message', command=self.printmessage)
        self.printbutton.pack(side=LEFT)

        self.quitbutton = Button(frame, text='Quit', command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print 'Here is a message'


root = Tk()
b = MikeButtons(root)
root.mainloop()