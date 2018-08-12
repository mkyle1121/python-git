from Tkinter import *


def donothing():
    print'ok ok I won\'t'


root = Tk()

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Project...', command=donothing)
submenu.add_command(label='New...', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=donothing)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Redo', command=donothing)

#The toolbar ********

toolbar = Frame(root, bg='blue')

insertbutt = Button(toolbar, text='Insert image', command=donothing)
insertbutt.pack(side=LEFT, padx=2, pady=2)
printbutt = Button(toolbar, text='Print', command=donothing)
printbutt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)




root.mainloop()