from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
win = Tk()
win.geometry("500x500")
win.title("this is a money calculator")
def msg():
    a = messagebox.showinfo("info","do you want to calculate the denomination count")
    if a == "ok":
        denomonation()

def denomonation():
        def calculate():
             amount = int(entry1.get())
             note2000 = amount//2000
             note500 = (amount%2000)//500
             note100 = ((amount%2000)%500)//100
             entry2000.insert(END,str(note2000))
             entry500.insert(END,str(note500))
             entry100.insert(END,str(note100))

        TOP1 = Toplevel()
        TOP1.geometry("500x500")
        label3 = Label(TOP1,text = "welocome to the calculator")
        label3.pack()
        label4 = Label(TOP1,text = "enter the amount")
        label4.pack()
        entry1 = Entry(TOP1)
        entry1.pack()
        button2 = Button(TOP1,text = "calculate",command = calculate)
        label5 = Label(TOP1,text = "here are the number of notes")
        button2.pack()
        label5.pack()
        label2000 = Label(TOP1,text = "2000")
        label2000.pack()
        entry2000 = Entry(TOP1)
        entry2000.pack()
        label500 = Label(TOP1,text = "500")
        label500.pack()
        entry500 = Entry(TOP1)
        entry500.pack()
        label100 = Label(TOP1,text = "100")
        label100.pack()
        entry100 = Entry(TOP1)
        entry100.pack()



#upload = Image.open("hgf.png")
#upload = Image.resize("300x200")
#img = ImageTk.PhotoImage(upload)
#label2 = Label(win,Image = img)
label1 = Label(win,text = "welocome to destruction calculator")
button1 = Button(win,text = "START",command = msg)
label1.pack(pady = 10)
#label2.pack(pady = 30)
button1.pack(pady = 60)
win.mainloop()