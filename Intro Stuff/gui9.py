from Tkinter import *

root = Tk()

photo = PhotoImage(file='mikeferrari.jpg')
label = Label(root, image=photo)
label.pack()

root.mainloop()
