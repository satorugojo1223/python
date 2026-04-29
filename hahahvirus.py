from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("virus")
win.geometry("300x400+500+100")
win.configure(bg = "Skyblue")

def msg():
    messagebox.showwarning("alert","virusfound")

label1 = Label(win,text = "quick and good virus scan (no scam for real)",fg = "black" ,bg = "green")
label1.place(x=60,y=150)
button1 = Button(win,relief="groove",bg = "grey",command = msg,text = "click me hahahahhahahhahahah",font = ("Times",12,"bold"))
button1.place(x=60,y=180)

win.mainloop()