from tkinter import *

class my_app():
    def __init__(self,app):
        self.app = app
        self.app.wm_title('Something App')
        # label1=Label(app,text='Label 1 stuff')
        # label1.grid(row=0)
        # button1=Button(app,text='button1')
        # button1.grid(row=0,column=1)
        for i in range(4):
            button=Button(app,text='button '+str(i))
            button.grid(row=i)
            label = Label(app, text='Label '+str(i))
            label.grid(row=i, column=1)
            entry=Entry(app,text='Entry '+str(i))
            entry.grid(row=i,column=2)



app=Tk()        #create Tk window object
my_app(app)     #pass Tk object into my object
app.mainloop()  #call Tk object's mainloop

