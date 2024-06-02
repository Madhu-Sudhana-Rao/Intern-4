import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        plen = int(length_entry.get())
        if plen < 12:
            raise ValueError("Password length should be at least 12 characters.")
        
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
        password = "".join(s[:plen])
        
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
