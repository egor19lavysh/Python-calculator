from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x550")
root.resizable(False, False)
root.title("Python calculator")
root["bg"] = "black"

def clear():
    entry.delete(0, END)
def update(symbol):
    expression = entry.get()
    entry.delete(0, END)
    if expression != "incorrect expression" and expression != "0":
        entry.insert(0, expression + symbol)
    else:
        entry.insert(0, symbol)

def calculate():
    expr = entry.get()
    try:
        answer = eval(expr)
    except:
        answer = "incorrect expression"
    entry.delete(0, END)
    entry.insert(0, answer)


frm = ttk.Frame(root)
frm.grid(column=4)


entry = Entry(root, font=("Arial", 27), justify="right", background="black", foreground="white", borderwidth=0)
entry.grid(row=0, column=0, columnspan=4, pady=110)


clear_btn = Button(root, text="C", background="#DBD6D6", width=10, height=3, command=lambda: clear())
clear_btn.grid(row=1, column=0)


command_buttons_horizontal = [
    "+/-", "%", "/",
]
col = 1
for button in command_buttons_horizontal:
    if col != 3:
        btn = Button(root, text=button, background="#DBD6D6", width=10, height=3, command=lambda b=button: update(b))
        btn.grid(row=1, column=col)
        col+=1
    else:
        btn = Button(root, text=button, background="orange", foreground="white", width=10, height=3, command=lambda b=button: update(b))
        btn.grid(row=1, column=col)
        col += 1


command_buttons_vertical = [
    "*", "-", "+", "=",
]
row = 2
for button in command_buttons_vertical:
    if button != "=":
        btn = Button(root, text=button, background="orange", foreground="white", width=10, height=3, command=lambda b=button: update(b))
        btn.grid(row=row, column=3)
        row+=1
    else:
        btn = Button(root, text=button, background="orange", foreground="white", width=10, height=3,
                     command=lambda: calculate())
        btn.grid(row=row, column=3)



buttons = [

    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
]

row = 2
col = 0
for button in buttons:
    btn = Button(root, text=button, background="grey", width=10, height=3, command=lambda b=button: update(b))
    btn.grid(row=row, column=col)

    if col == 2:
        col = 0
        row += 1
    else:
        col += 1

zero = Button(root, text="0", background="grey", width=25, height=3, command=lambda: update("0"))
zero.grid(row=5, column=0, columnspan=2)

dot = Button(root, text=".", background="grey", width=10, height=3, command=lambda: update("."))
dot.grid(row=5, column=2)


root.mainloop()