def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Temperature Converter")
    choice = input("Convert from (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius? Enter 1 or 2: ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Temperature in Fahrenheit: {fahrenheit}")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Temperature in Celsius: {celsius}")
    else:
        print("Invalid choice")

temperature_converter()
