import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except:
        messagebox.showerror("Error", "Enter a valid number")

root = tk.Tk()
root.title("Length Converter")
root.geometry("300x200")

tk.Label(root, text="Enter length in inches").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()