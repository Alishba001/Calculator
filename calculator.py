import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."


def power(a, b):
    return math.pow(a, b)


def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Invalid input for square root."


def calculate():
    print("Unique Calculator")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Quit")

    while True:
        choice = input("Enter the operation number (1-7): ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print("Result:", result)

        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print("Result:", result)

        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply(num1, num2)
            print("Result:", result)

        elif choice == "4":
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            result = divide(num1, num2)
            print("Result:", result)

        elif choice == "5":
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            result = power(num1, num2)
            print("Result:", result)

        elif choice == "6":
            num = float(input("Enter the number: "))
            result = sqrt(num)
            print("Result:", result)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1-7.")


calculate()
