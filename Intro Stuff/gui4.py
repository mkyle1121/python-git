from Tkinter import *

root = Tk()

def printname(event):
    print 'Hello my name is Mike'

button_1 = Button(root, text="Print Name", #command=printname)
button_1.bind('<Button-1>', printname) # can take this out
button_1.pack()


root.mainloop()