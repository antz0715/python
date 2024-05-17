def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):

    if y == 0:
        return "Error, cannot divide by 0"
    else:
        return x / y
    
print("Select Operation")
print("1. ADD")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4) ")

num1 = input("Enter the first number ")
num2 = input("enter the second number ")


if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}") 
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} * {num2} = {divide(num1, num2)}")
else:
    print("please enter a valid choice")