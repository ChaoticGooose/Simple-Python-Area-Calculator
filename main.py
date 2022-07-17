from math import pi
from os import name, system
from time import sleep
import tkinter as tk
import tkinter.ttk as ttk


def btnRectangleDown():
    print("Rectangle")


def main():
    root = tk.Tk()
    root.title("Area Calculator")
    root.geometry("300x300")

    btnframe = ttk.Frame(root)
    rectangle_btn = ttk.Button(btnframe, text="Rectangle", command=btnRectangleDown)
    rectangle_btn.grid(column=1, row=0)
    btnframe.grid()

    root.mainloop()


# checks that program is not running as library then runs main function
if __name__ == '__main__':
    main()
