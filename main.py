from math import pi
from os import name, system
from time import sleep
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()


def rectangleView():
    # Hides the other views
    triangle_input.grid_forget()
    trapezium_input.grid_forget()
    circle_input.grid_forget()

    # create width and height variables
    width = tk.StringVar()
    hight = tk.StringVar()

    # create width and height input fields
    widthInput = ttk.Entry(rectangle_input, textvariable=width)
    heightInput = ttk.Entry(rectangle_input, textvariable=hight)

    # Label the input fields
    heightLbl = ttk.Label(rectangle_input, text="Height:")
    widthLbl = ttk.Label(rectangle_input, text="Width:")

    # grid the widgets
    heightLbl.grid(row=0, column=0)
    widthLbl.grid(row=1, column=0)
    widthInput.grid(row=0, column=1)
    heightInput.grid(row=1, column=1)
    rectangle_input.grid(column=1, row=2)


def triangleView():
    # hides the other views
    rectangle_input.grid_forget()
    trapezium_input.grid_forget()
    circle_input.grid_forget()

    # create width and height variables
    base = tk.StringVar()
    height = tk.StringVar()

    # create base and height input fields
    baseInput = ttk.Entry(triangle_input, textvariable=base)
    heightInput = ttk.Entry(triangle_input, textvariable=height)

    # Label the input fields
    baselbl = ttk.Label(triangle_input, text="Base:")
    heightlbl = ttk.Label(triangle_input, text="Height:")

    # Label the input fields
    baselbl.grid(row=0, column=0)
    heightlbl.grid(row=1, column=0)
    baseInput.grid(row=0, column=1)
    heightInput.grid(row=1, column=1)
    triangle_input.grid(column=1, row=2)


def trapeziumView():
    # hides the other views
    rectangle_input.grid_forget()
    triangle_input.grid_forget()
    circle_input.grid_forget()

    # create top, bottom and height variables
    top = tk.StringVar()
    bottom = tk.StringVar()
    height = tk.StringVar()

    # create top, bottom and height input fields
    topInput = ttk.Entry(trapezium_input, textvariable=top)
    bottomInput = ttk.Entry(trapezium_input, textvariable=bottom)
    heightInput = ttk.Entry(trapezium_input, textvariable=height)

    # Label the input fields
    toplbl = ttk.Label(trapezium_input, text="Top:")
    bottomlbl = ttk.Label(trapezium_input, text="Bottom:")
    heightlbl = ttk.Label(trapezium_input, text="Height:")

    # grid the widgets
    toplbl.grid(row=0, column=0)
    bottomlbl.grid(row=1, column=0)
    heightlbl.grid(row=2, column=0)
    topInput.grid(row=0, column=1)
    bottomInput.grid(row=1, column=1)
    heightInput.grid(row=2, column=1)
    trapezium_input.grid(column=1, row=2)


def circle():
    # hides the other views
    rectangle_input.grid_forget()
    triangle_input.grid_forget()
    trapezium_input.grid_forget()

    # create radius variable
    radius = tk.StringVar()

    # create radius input field
    radiusInput = ttk.Entry(circle_input, textvariable=radius)

    # Label the input fields
    radiuslbl = ttk.Label(circle_input, text="Radius:")

    # grid the widgets
    radiuslbl.grid(row=0, column=0)
    radiusInput.grid(row=0, column=1)
    circle_input.grid(column=1, row=2)


if __name__ == '__main__':
    # Sets up window
    root.title("Area Calculator")
    root.geometry("300x300")
    root.resizable(False, False)

    radio_frame = ttk.Frame(root)
    shape = tk.StringVar()

    # Creates radio buttons and input frame
    rectangle = ttk.Radiobutton(radio_frame, text="Rectangle", variable=shape, value="rectangle", command=rectangleView)
    rectangle.pack(anchor=tk.W)
    rectangle_input = tk.Frame(root)

    triangle = ttk.Radiobutton(radio_frame, text="Triangle", variable=shape, value="triangle", command=triangleView)
    triangle.pack(anchor=tk.W)
    triangle_input = tk.Frame(root)

    circle = ttk.Radiobutton(radio_frame, text="Circle", variable=shape, value="circle", command=circle)
    circle.pack(anchor=tk.W)
    circle_input = tk.Frame(root)

    trapezium = ttk.Radiobutton(radio_frame, text="Trapezium", variable=shape, value="trapezium", command=trapeziumView)
    trapezium.pack(anchor=tk.W)
    trapezium_input = tk.Frame(root)

    # Creates output fields
    output_lbl = ttk.Label(radio_frame, text="Area: ")
    output_lbl.pack(side=tk.LEFT)

    radio_frame.grid(column=1, row=1)
    radio_frame.grid()

    root.mainloop()
