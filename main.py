from math import pi
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()


def rectangleView():  # shows all widgets in view
    # grid the widgets
    rectangle_heightLbl.grid(row=0, column=0)
    rectangle_widthLbl.grid(row=1, column=0)
    rectangle_widthInput.grid(row=0, column=1)
    rectangle_heightInput.grid(row=1, column=1)
    rectangle_input.grid(column=1, row=2)

    # Hides the other views
    triangle_input.grid_forget()
    trapezium_input.grid_forget()
    circle_input.grid_forget()




def triangleView():  # shows all widgets in view
    # grid the widgets
    triangle_baselbl.grid(row=0, column=0)
    triangle_heightlbl.grid(row=1, column=0)
    triangle_baseInput.grid(row=0, column=1)
    triangle_heightInput.grid(row=1, column=1)
    triangle_input.grid(column=1, row=2)

    # hides the other views
    rectangle_input.grid_forget()
    trapezium_input.grid_forget()
    circle_input.grid_forget()




def trapeziumView():  # shows all widgets in view
    # grid the widgets
    trapezium_toplbl.grid(row=0, column=0)
    trapezium_bottomlbl.grid(row=1, column=0)
    trapezium_heightlbl.grid(row=2, column=0)
    trapezium_topInput.grid(row=0, column=1)
    trapezium_bottomInput.grid(row=1, column=1)
    trapezium_heightInput.grid(row=2, column=1)
    trapezium_input.grid(column=1, row=2)

    # hides the other views
    rectangle_input.grid_forget()
    triangle_input.grid_forget()
    circle_input.grid_forget()


def circle():  # shows all widgets in view
    # grid the widgets
    circle_radiuslbl.grid(row=0, column=0)
    circle_radiusInput.grid(row=0, column=1)
    circle_input.grid(column=1, row=2)

    # hides the other views
    rectangle_input.grid_forget()
    triangle_input.grid_forget()
    trapezium_input.grid_forget()


def calculateArea(shape):
    if shape == "rectangle":
        width = float(rectangle_widthInput.get())
        height = float(rectangle_heightInput.get())
        area = width * height
        perimeter = 2 * (width + height)
        Area.configure(text="Area: " + str(area))
        Perimeter.configure(text="Perimeter: " + str(perimeter))
    elif shape == "triangle":
        base = float(triangle_baseInput.get())
        height = float(triangle_heightInput.get())
        area = (base * height) / 2
        perimeter = base + height + (base * height)
        Area.configure(text="Area: " + str(area))
        Perimeter.configure(text="Perimeter: " + str(perimeter))
    elif shape == "trapezium":
        top = float(trapezium_topInput.get())
        bottom = float(trapezium_bottomInput.get())
        height = float(trapezium_heightInput.get())
        area = ((top + bottom) * height) / 2
        perimeter = top + bottom + (top * bottom)
        Area.configure(text="Area: " + str(area))
        Perimeter.configure(text="Perimeter: " + str(perimeter))
    elif shape == "circle":
        radius = float(circle_radiusInput.get())
        area = pi * (radius ** 2)
        perimeter = 2 * pi * radius
        Area.configure(text="Area: " + str(area))
        Perimeter.configure(text="Perimeter: " + str(perimeter))


if __name__ == '__main__':
    # Sets up window
    root.title("Area Calculator")
    root.geometry("270x235")
    root.resizable(False, False)

    radio_frame = ttk.Frame(root)
    shape = tk.StringVar(None, "rectangle")
    output = ttk.Frame(root)

    # Creates radio buttons and input frame
    rectangle = ttk.Radiobutton(radio_frame, text="Rectangle", variable=shape, value="rectangle", command=rectangleView)
    rectangle.grid(row=0, column=0, sticky="W")
    rectangle_input = tk.Frame(root)

    # create width and height variables
    rectangle_width = tk.StringVar()
    rectangle_hight = tk.StringVar()

    # create width and height input fields
    rectangle_widthInput = ttk.Entry(rectangle_input, textvariable=rectangle_width)
    rectangle_heightInput = ttk.Entry(rectangle_input, textvariable=rectangle_hight)

    # Label the input fields
    rectangle_heightLbl = ttk.Label(rectangle_input, text="Height:")
    rectangle_widthLbl = ttk.Label(rectangle_input, text="Width:")

    triangle = ttk.Radiobutton(radio_frame, text="Triangle", variable=shape, value="triangle",
                               command=triangleView)  # creates triangle radio button
    triangle.grid(row=1, column=0, sticky="W")
    triangle_input = tk.Frame(root)

    # create width and height variables
    triangle_base = tk.StringVar()
    triangle_height = tk.StringVar()

    # create base and height input fields
    triangle_baseInput = ttk.Entry(triangle_input, textvariable=triangle_base)
    triangle_heightInput = ttk.Entry(triangle_input, textvariable=triangle_height)

    # Label the input fields
    triangle_baselbl = ttk.Label(triangle_input, text="Base:")
    triangle_heightlbl = ttk.Label(triangle_input, text="Height:")

    circle = ttk.Radiobutton(radio_frame, text="Circle", variable=shape, value="circle",
                             command=circle)  # creates circle radio button
    circle.grid(row=2, column=0, sticky="W")
    circle_input = tk.Frame(root)
    # create radius variable
    circle_radius = tk.StringVar()

    # create radius input field
    circle_radiusInput = ttk.Entry(circle_input, textvariable=circle_radius)

    # Label the input fields
    circle_radiuslbl = ttk.Label(circle_input, text="Radius:")

    trapezium = ttk.Radiobutton(radio_frame, text="Trapezium", variable=shape, value="trapezium",
                                command=trapeziumView)  # creates a radio button for trapezium
    trapezium.grid(row=3, column=0, sticky="W")
    trapezium_input = tk.Frame(root)

    # create top, bottom and height variables
    trapezium_top = tk.StringVar()
    trapezium_bottom = tk.StringVar()
    trapezium_height = tk.StringVar()

    # create top, bottom and height input fields
    trapezium_topInput = ttk.Entry(trapezium_input, textvariable=trapezium_top)
    trapezium_bottomInput = ttk.Entry(trapezium_input, textvariable=trapezium_bottom)
    trapezium_heightInput = ttk.Entry(trapezium_input, textvariable=trapezium_height)

    # Label the input fields
    trapezium_toplbl = ttk.Label(trapezium_input, text="Top:")
    trapezium_bottomlbl = ttk.Label(trapezium_input, text="Bottom:")
    trapezium_heightlbl = ttk.Label(trapezium_input, text="Height:")

    # calculate button
    calculate = ttk.Button(root, text="Calculate", command=lambda: calculateArea(shape.get()))
    calculate.grid(column=1, row=3)

    # Creates output fields
    Area = ttk.Label(output, text="Area: ")
    Perimeter = ttk.Label(output, text="Perimeter: ")
    Area.grid(column=0, row=1)
    Perimeter.grid(column=0, row=2)

    radio_frame.grid(column=1, row=1)
    radio_frame.grid()
    output.grid(column=1, row=4)

    rectangleView()

    root.mainloop()
