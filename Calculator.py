import tkinter as tk
from tkinter import ttk
from tkinter import *

# Sets the title of the GUI
master = tk.Tk()
master.title('Calculator')

# The add equation button
def add():
    sumNum = (firstNumber.get()) + (secondNumber.get())
    output = Label(master, text = sumNum, width = 20)
    output.place(x = 250, y = 68, anchor = 'center')

# The subtract equation button
def subtract():
    differenceNum = (firstNumber.get()) - (secondNumber.get())
    output = Label(master, text = differenceNum, width = 20)
    output.place(x = 250, y = 68, anchor = 'center')

# The multiplication equation button
def multiply():
    multipleNum = (firstNumber.get()) * (secondNumber.get())
    output = Label(master, text = multipleNum, width = 20)
    output.place(x = 250, y = 68, anchor = 'center')
    
# The division equation button
def divide():
    try:
        divisionNum = (firstNumber.get()) / (secondNumber.get())
        output = Label(master, text = divisionNum, width = 20)
        output.place(x = 250, y = 68, anchor = 'center')
    except ZeroDivisionError:
        output = Label(master, text = 'You can not divide by 0', width = 20)
        output.place(x = 250, y = 68, anchor = 'center')
    
# The modulo equation button
def modulo():
    try:
        moduloNum = (firstNumber.get()) % (secondNumber.get())
        output = Label(master, text = moduloNum, width = 20)
        output.place(x = 250, y = 68, anchor = 'center')
    except ZeroDivisionError:
        output = Label(master, text = 'You can not modulo by 0', width = 20)
        output.place(x = 250, y = 68, anchor = 'center')

# Creates the Entry boxes for the numbers
firstNumber = tk.IntVar()
firstNum = ttk.Entry(master, width = 12, textvariable = firstNumber)
firstNum.grid(column = 2, row = 0)

secondNumber = tk.IntVar()
secondNum = ttk.Entry(master, width = 12, textvariable = secondNumber)
secondNum.grid(column = 4, row = 0)

# Adds a button to the master
add = ttk.Button(master, text = '+', command = add)
add.grid(column = 1, row = 8)

# Adds a subtraction button
subtract = ttk.Button(master, text = '-', command = subtract)
subtract.grid(column = 2, row = 8)

# Adds a multiplication button
multiply = ttk.Button(master, text = 'x', command = multiply)
multiply.grid(column = 3, row = 8)

# Adds a division button
division = ttk.Button(master, text = '/', command = divide)
division.grid(column = 4, row = 8)

# Adds a modulo button
modulo = ttk.Button(master, text = '%', command = modulo)
modulo.grid(column = 5, row = 8)

# Sets the size of the calculator window 
master.geometry('520x80')

# Main loop for the program
master.mainloop()
