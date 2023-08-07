import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_var.get())
    if length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return
    
    use_digits = digits_var.get()
    use_letters = letters_var.get()
    use_special = special_var.get()
    
    if not (use_digits or use_letters or use_special):
        messagebox.showerror("Error", "Select at least one character type.")
        return
    
    characters = ""
    if use_digits:
        characters += string.digits
    if use_letters:
        characters += string.ascii_letters
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_var = tk.StringVar(value="12")
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()

letters_var = tk.BooleanVar()
letters_check = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_check.pack()

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 16))
result_label.pack()

root.mainloop()
