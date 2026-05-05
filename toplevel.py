from tkinter import *
win = Tk()
win.geometry("200x300")
def TOP():
    TOP1 = Toplevel()
    TOP1.geometry("100x200")
    label2 = Label(TOP1,text = "This is the Top level window")
    label2.pack()
win.title("main")
label1 = Label(win,text = "This is the Main window")
button = Button(win,text = "click me",relief="groove",command = TOP)
label1.pack()
button.pack()

win.mainloop()