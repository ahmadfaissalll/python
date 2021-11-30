import tkinter as tk
from tkinter import messagebox

# window setup
root_window = tk.Tk(className=" Binary To Decimal Converter")

# size
HORIZONTAL, VERTICAL = '700', '450'
root_window.geometry(F'{HORIZONTAL}x{VERTICAL}')

HORIZONTAL = VERTICAL = False
root_window.resizable(HORIZONTAL, VERTICAL)


caption = tk.Label(root_window, text="Binary (separate with . (dot))", font=("Arial", 13)).pack(pady=10)

# user input
inputBinary = tk.Entry(fg="#000", bg='lightblue', width='37', font=("Arial", 11))
inputBinary.pack(pady=3)

def binary_to_decimal(binary):

    pangkat = len(binary) - 1

    decimal_result = 0

    for bit in binary[::-1]:
        decimal_result += int(bit) * (pow(2, pangkat))
        pangkat -= 1

    return str(decimal_result)

def displaying_converting_result():
    try:
        if (inputBinary.get()):
            binary_result.config(text=f"Decimal: {'.'.join(map(binary_to_decimal, inputBinary.get().strip('. ').split('.')))}")
    except ValueError:
        messagebox.showerror(title="Error", message="Invalid Input")


myBtn = tk.Button(text="Convert", command=displaying_converting_result, font=("Arial", 13), padx='10' ,pady="1.5").pack(pady=5)

binary_result = tk.Label(root_window, font=("Arial", 12))
binary_result.pack(pady=15)

root_window.mainloop()