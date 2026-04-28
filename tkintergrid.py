from tkinter import *
win = Tk()
win.title("number pad")
win.geometry("300x400")
win.configure(bg = "skyblue")
t = [[7,8,9],[4,5,6],[1,2,3],[0,'#','*']]
for i in range(4):
    win.rowconfigure(i,weight = 3, minsize = 80)
    for j in range(3):
        win.columnconfigure(j,weight=20 ,minsize = 70)
        label1 = Label(text = t[i][j],relief = "ridge",bg = "beige",bd = 3)
        label1.grid(row = i ,column = j)
    
win.mainloop()