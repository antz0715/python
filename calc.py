def add(x, y, z):
    #Add Function
    return x + y + z

def subtract(x, y):
    #Subtract Function
    return x - y

def multiply(x, y):
    #Multiply Function 
    return x * y

def divide(x, y):
    #Divide Function
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# User input
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))  # 12.3 1.2 7     int--- 7 7 2 4 421 5
num2 = float(input("Enter second number: "))


# Perform the operation
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2,)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")
