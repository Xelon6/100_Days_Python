import tkinter as tk

# Function to update the display with the typed number
def typeAnswer(value):
    current = summe["text"]
    # Append the typed number to the current value
    summe["text"] = current + str(value)

# Function to handle arithmetic operations
def calcAnswer(op):
    global answer, lastNumber, operator
    # Store the current value and operator for calculation
    lastNumber = float(summe["text"])
    operator = op
    summe["text"] = ""

# Function to calculate the result
def calculate():
    global answer, lastNumber, operator
    # Get the current value
    current = float(summe["text"])
    # Perform the operation based on the stored operator
    if operator == "+":
        answer = lastNumber + current
    elif operator == "-":
        answer = lastNumber - current
    elif operator == "*":
        answer = lastNumber * current
    elif operator == "/":
        # Handle division by zero
        if current == 0:
            summe["text"] = "Error"
            return
        else:
            answer = lastNumber / current
    summe["text"] = str(answer)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")

# Create a label to display the current input or result
summe = tk.Label(window, text="", anchor="e", font=("Helvetica", 16))
summe.grid(row=0, column=0, columnspan=4, sticky="ew")

# Define button labels and their positions
buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("4", 2, 0),
    ("5", 2, 1), ("6", 2, 2), ("7", 3, 0), ("8", 3, 1),
    ("9", 3, 2), ("0", 4, 1), ("+", 1, 3), ("-", 2, 3),
    ("*", 3, 3), ("/", 4, 3), ("=", 4, 2)
]

# Create buttons using a loop
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, command=lambda t=text: typeAnswer(t))
    button.grid(row=row, column=col, sticky="nsew")

# Assign commands for arithmetic operation buttons
for op in ("+", "-", "*", "/"):
    button = [b for b in window.grid_slaves() if b.grid_info()["column"] == 3 and b.cget("text") == op][0]
    button.config(command=lambda o=op: calcAnswer(o))

# Assign command for the equals button
equals_button = [b for b in window.grid_slaves() if b.grid_info()["row"] == 4 and b.grid_info()["column"] == 2][0]
equals_button.config(command=calculate)

# Configure row and column weights for grid resizing
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
window.mainloop()
