from math import pi
from os import name, system
from time import sleep
import tkinter as tk
import tkinter.ttk as ttk

def btnRectangleDown():
    global width, length
    try:
        # Requests user input
        width = float(input("Input Width: "))
        length = float(input("Input Length: "))
    # If a non-float value is inputted throws error and reruns function
    except ValueError:
        print('\033[91m' + "Value is not a number" + '\033[0m')
        btnRectangleDown()
    output_lbl["text"] = "Area: " + str(width * length)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Area Calculator")
    root.geometry("300x300")

    btnframe = ttk.Frame(root)
    outputframe = ttk.Frame(root)
    rectangle_btn = ttk.Button(btnframe, text="Rectangle", command=btnRectangleDown)
    rectangle_btn.pack(side=tk.LEFT)

    output_lbl = ttk.Label(outputframe, text="Area: ")
    output_lbl.pack(side=tk.LEFT)

    rectangle_btn.grid(column=1, row=0)
    outputframe.grid(column=1, row=1)
    btnframe.grid()
    root.mainloop()

