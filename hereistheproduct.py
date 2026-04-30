import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        product = num1 * num2
        result_label.config(text=f"Product: {product}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

# Window
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x220")

# Inputs
tk.Label(root, text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Button
tk.Button(root, text="Calculate Product", command=calculate_product).pack(pady=10)

# Result
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()