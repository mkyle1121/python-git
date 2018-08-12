from Tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Click Me!', fg='red')
button2 = Button(topFrame, text='button 2', fg='blue')
button3 = Button(topFrame, text='button 3!', fg='green')
button4 = Button(bottomFrame, text='button fo', fg='purple')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()
