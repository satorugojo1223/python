from tkinter import *
from datetime import date
root = Tk()
root.geometry("400x400")
root.title("MY FIRST TKINTER")
root.configure(bg = "Skyblue")
def start():
    name = entry1.get()
    name = "welcome "+name+"\n" "Todays date is " + str(date.today())
    text1.delete("1.0",END)
    text1.insert("1.0",name)

Label1 = Label(text = "Name" , bg = "beige", fg = "brown",font = ("Arial",13,"bold"))
Label1.pack(pady = 20)
entry1 = Entry()
entry1.pack(pady = 10)
button1 = Button(text = "Start" , bg = "LightGreen", fg = "Pink",font = ("Arial",13,"bold"),command = start)
button1.pack(pady = 10)
text1 = Text(width = 30 ,height = 7, bg = "Grey", fg = "White",font = ("Arial",13,"bold"))
text1.pack(pady = 10)
root.mainloop()