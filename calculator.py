import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def power(x, y):
    for i in range(y):
        x = x*x
    return x


def perform_operation():
    user_input = operation_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    
    if user_input == "add":
        result_label.config(text=f"Result: {add(num1, num2)}")
    elif user_input == "subtract":
        result_label.config(text=f"Result: {subtract(num1, num2)}")
    elif user_input == "multiply":
        result_label.config(text=f"Result: {multiply(num1, num2)}")
    elif user_input == "divide":
        result_label.config(text=f"Result: {divide(num1, num2)}")
    elif user_input == "ower":
        result_label.config(text=f"Result: {power(num1, num2)}")
    else:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Calculator")

operation_var = tk.StringVar()
operation_var.set("add")

frame = tk.Frame(root)
frame.pack()

operation_label = tk.Label(frame, text="Choose operation:")
operation_label.grid(row=0, column=0)

operation_menu = tk.OptionMenu(frame, operation_var, "add", "subtract", "multiply", "divide", "power")
operation_menu.grid(row=0, column=1)

num1_label = tk.Label(frame, text="Enter first number:")
num1_label.grid(row=1, column=0)

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=1, column=1)

num2_label = tk.Label(frame, text="Enter second number:")
num2_label.grid(row=2, column=0)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=2, column=1)

calculate_button = tk.Button(frame, text="Calculate", command=perform_operation)
calculate_button.grid(row=3, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
