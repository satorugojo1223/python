from tkinter import *
windows = Tk()
windows.title("event")
windows.configure(bg = "white")
windows.geometry("400x300")

def handleclick(event):
    print("a button has been pressed")

def key_press(event):
    print(event.char)

windows.bind("<Key>",key_press)
button1 = Button(windows,text = "press me!",fg = "grey",bg = "Lightblue",relief = "groove")
button1.place(x=150,y=150)
button1.bind("<Button-1>",handleclick)

windows.mainloop()