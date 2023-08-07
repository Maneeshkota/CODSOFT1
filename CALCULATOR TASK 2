import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x500")
root.title("Simple Calculator")

screen = tk.StringVar()
screen.set("")

entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_value = 1
col_value = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1
    btn.bind("<Button-1>", on_button_click)

root.mainloop()
