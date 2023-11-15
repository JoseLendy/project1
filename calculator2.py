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
        result = eval(calculation)
        if float(result).is_integer():
            calculation = str(int(result))
        else:
            calculation = str(result)
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

def backspace(self):
#check if all has been removed
#make sure you import the re module
    if re.match(r'\d$', self.current):
        self.display(0)
        self.new_num = True
    else:
        self.current = self.current[:-1]    
        self.display(self.current)

def exit():
    root.destroy()

def on_key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/()":
        add(key)
    elif event.keysym == "Return":
        evaluate()
    elif event.keysym == "Backspace":
        backspace()
    elif event.keysym == "Escape":
        clear()
    elif event.keysym == "c":
        exit()

root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height = 2, width = 16, font = ("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text = "1", command = lambda: add(1), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(root, text = "2", command = lambda: add(2), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(root, text = "3", command = lambda: add(3), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_3.grid(row = 2, column = 3)
btn_4 = tk.Button(root, text = "4", command = lambda: add(4), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(root, text = "5", command = lambda: add(5), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(root, text = "6", command = lambda: add(6), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_6.grid(row = 3, column = 3)
btn_7 = tk.Button(root, text = "7", command = lambda: add(7), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(root, text = "8", command = lambda: add(8), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(root, text = "9", command = lambda: add(9), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_9.grid(row = 4, column = 3)
btn_0 = tk.Button(root, text = "0", command = lambda: add(0), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_0.grid(row = 5, column = 2)
btn_plus = tk.Button(root, text = "+", command = lambda: add("+"), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_plus.grid(row = 2, column = 4)
btn_minus = tk.Button(root, text = "-", command = lambda: add("-"), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_minus.grid(row = 3, column = 4)
btn_open = tk.Button(root, text = "(", command = lambda: add("("), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_open.grid(row = 5, column = 1)
btn_close = tk.Button(root, text = ")", command = lambda: add(")"), width = 5, font=("Arial", 14), bg="orange", fg="white")
btn_close.grid(row = 5, column = 3)
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