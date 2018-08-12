from tkinter import *

window=Tk()

def km_to_miles():
    miles=float(e1_value.get())*1.606
    t1.insert(END,miles)

b1=Button(window,text="Execute",command=km_to_miles)
#b1.pack()
b1.grid(row=0,column=0)

e1_value=StringVar()    #set e1 value with stringvar, look this up
e1=Entry(window,textvariable=e1_value)   #grab information from an entry box!!
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)  #normal text box is large
t1.grid(row=0,column=2)

window.mainloop()