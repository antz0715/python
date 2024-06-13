import math

def add(x, y):
    # Add Function
    return x + y 

def subtract(x, y):
    # Subtract Function
    return x - y

def multiply(x, y):
    # Multiply Function 
    return x * y

def divide(x, y):
    # Divide Function
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    # Power Function
    return math.pow(x, y)

def sqrt(x):
    # Square Root Function
    return math.sqrt(x)

def sine(x):
    # Sine Function
    radians = math.radians(x)
    sine_value = math.sin(radians)
    return sine_value, radians

def cosine(x):
    # Cosine Function
    radians = math.radians(x)
    cosine_value = math.cos(radians)
    return cosine_value, radians

while True:
    # User input
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice == '9':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")

    elif choice == '6':
        num = float(input("Enter number: "))
        print(f"Square root of {num} = {sqrt(num)}")

    elif choice == '7':
        angle = float(input("Enter angle in degrees: "))
        sine_value, radians = sine(angle)
        print(f"Sine of {angle} degrees = {sine_value} (in radians: {radians})")

    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        cosine_value, radians = cosine(angle)
        print(f"Cosine of {angle} degrees = {cosine_value} (in radians: {radians})")

    else:
        print("Invalid input. Please try again.")
