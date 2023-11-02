import tkinter as tk

calculation = ""

def parse_string(symbol):
    symbol = symbol.replace("*", "x")
    symbol = symbol.replace("/", "÷")
    return symbol

def add(symbol):
    global calculation
    calculation += str(symbol)
    update_display()

def delete():
    global calculation
    calculation = calculation[:-1]
    update_display()

def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        update_display()
    except:
        clear()
        text_result.insert(1.0, "Error")

def clear():
    global calculation
    calculation = ""
    update_display()

def update_display():
    text_result.delete(1.0, "end")
    text_result.insert(1.0, parse_string(calculation))

def on_key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/()":
        add(key)
    elif event.keysym == "Return":
        evaluate()
    elif event.keysym == "Backspace":
        delete()
    elif event.keysym == "Escape":
        clear()

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=5)

buttons = [
    ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
    ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
    ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
    ("0", 5, 2),
    ("+", 2, 4), ("-", 3, 4),
    ("(", 5, 1), (")", 5, 3),
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, command=lambda t=text: add(t), width=5, font=("Arial", 14), bg="orange", fg="white")
    button.grid(row=row, column=column)

btn_times = tk.Button(root, text="x", command=lambda: add("*"), width=5, font=("Arial", 14), bg="orange", fg="white")
btn_times.grid(row=4, column=4)
btn_div = tk.Button(root, text="÷", command=lambda: add("/"), width=5, font=("Arial", 14), bg="orange", fg="white")
btn_div.grid(row=5, column=4)
btn_equal = tk.Button(root, text="=", command=evaluate, width=11, font=("Arial", 14), bg="green", fg="black")
btn_equal.grid(row=6, column=3, columnspan=2)
btn_ac = tk.Button(root, text="AC", command=clear, width=5, font=("Arial", 14), bg="red", fg="black")
btn_ac.grid(row=6, column=1, columnspan=1)
btn_del = tk.Button(root, text="DEL", command=delete, width=5, font=("Arial", 14), bg="yellow", fg="black")
btn_del.grid(row=6, column=2, columnspan=1)

root.bind("<Key>", on_key_press)
root.mainloop()
