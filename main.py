from math import pi
from os import name, system
from time import sleep


# Calc Functions
def rectangle():
    global width, length
    try:
        # Requests user input
        width = float(input("Input Width: "))
        length = float(input("Input Length: "))
    # If a non-float value is inputted throws error and reruns function
    except ValueError:
        print('\033[91m' + "Value is not a number" + '\033[0m')
        rectangle()
    return width * length


def triangle():
    global height, base
    try:
        # Requests user input
        height = int(input("Input Height: "))
        base = int(input("Input Base: "))
    # If a non-float value is inputted throws error and reruns function
    except ValueError:
        print('\033[91m' + "Value is not a number" + '\033[0m')
        triangle()
    return 0.5 * height * base


def trapezium():
    global top, bottom, height
    # Requests user input
    try:
        top = int(input("Input Top: "))
        bottom = int(input("Input Bottom: "))
        height = int(input("Input Height: "))
    # If a non-float value is inputted throws error and reruns function
    except ValueError:
        print('\033[91m' + "Value is not a number" + '\033[0m')
        trapezium()
    return 0.5 * (top + bottom) * height


def circle():
    global radius
    # Requests user input
    try:
        radius = int(input("Input Radius: "))
    # If a non-float value is inputted throws error and reruns function
    except ValueError:
        print('\033[91m' + "Value is not a number" + '\033[0m')

    return pi * radius ** 2


def main():
    # User input
    shape = str(input("Input Shape Type (Rectangle/Triangle/Trapezium/Circle): ").lower())

    # Call function
    if shape == "rectangle":
        print(rectangle())
    elif shape == "triangle":
        print(triangle())
    elif shape == "trapezium":
        print(trapezium())
    elif shape == "circle":
        print(circle())
    else:
        # anything not in the list throws error and reruns function
        print('\033[91m' + "INVALID" + '\033[0m')
        sleep(0.5)
        system('cls' if name == 'nt' else 'clear')
        main()


# checks that program is not running as library then runs main function
if __name__ == '__main__':
    main()