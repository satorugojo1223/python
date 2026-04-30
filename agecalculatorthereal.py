import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        d = int(entry_day.get())
        m = int(entry_month.get())
        y = int(entry_year.get())

        today = date.today()
        birth = date(y, m, d)

        age = today.year - birth.year

        # adjust if birthday hasn't come yet this year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1

        result_label.config(text=f"Your Age: {age} years")

    except:
        messagebox.showerror("Error", "Enter valid date")

# Window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("320x250")

# Inputs
tk.Label(root, text="Day").pack()
entry_day = tk.Entry(root)
entry_day.pack()

tk.Label(root, text="Month").pack()
entry_month = tk.Entry(root)
entry_month.pack()

tk.Label(root, text="Year").pack()
entry_year = tk.Entry(root)
entry_year.pack()

# Button
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Result
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()