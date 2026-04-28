from tkinter import *
win = Tk()
win.title('email')
win.geometry("300x400")
win.configure(bg = "Skyblue")
def login():
    name = entry1.get()
    Text1.delete("1.0","end")
    Text1.insert("1.0",name+"login success")
frame1 = Frame(win,bg = "grey" , width = 300 , height = 400 ,bd = 3)
frame1.pack()

label1 = Label(frame1,text = "USERNAME",bg = "DarkGreen" ,fg = "Lime", height = 1 ,bd = 3)
label2 = Label(frame1,text = "PASSWORD",bg = "DarkGreen" ,fg = "Lime", height = 1 ,bd = 3)
entry1 = Entry(frame1)
entry2 = Entry(frame1,show = "*")
button1 = Button(frame1,text = "LOGIN",bg = "Blue" ,fg = "Red", height = 1 ,bd = 3, command = login)

label1.place(x = 10,y = 10)
label2.place(x = 10,y = 40)
entry1.place(x = 100, y = 10)
entry2.place(x = 100, y = 40)
button1.place(x = 45,y = 70)

Text1 = Text(win,bg = "Skyblue" ,fg = "Lime", height = 8 , width = 150 , bd = 3)
Text1.place(x = 10 ,y = 100)

win.mainloop()