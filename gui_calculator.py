import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Select an operation"

        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
window = tk.Tk()
window.title("Simple Calculator")

# Inputs
tk.Label(window, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

# Dropdown for operation
operation_var = tk.StringVar(window)
operation_var.set("Add")  # default value
tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide").grid(row=2, column=0, columnspan=2)

# Calculate button
tk.Button(window, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

# Result
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Run the app
window.mainloop()
