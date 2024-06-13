def binary_to_decimal(binary_str):
    """Convert a binary string to a decimal number."""
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_binary(decimal_num):
    """Convert a decimal number to a binary string."""
    if decimal_num == 0:
        return "0"
    binary_str = ""
    while decimal_num > 0:
        binary_str = str(decimal_num % 2) + binary_str
        decimal_num = decimal_num // 2
    return binary_str

def main():
    print("Binary to Decimal and Decimal to Binary Converter")
    print("1. Convert Binary to Decimal")
    print("2. Convert Decimal to Binary")
    
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        binary_str = input("Enter a binary number: ")
        try:
            decimal_result = binary_to_decimal(binary_str)
            print(f"The decimal representation of {binary_str} is {decimal_result}.")
        except ValueError:
            print("Invalid binary number.")
    elif choice == '2':
        try:
            decimal_num = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(decimal_num)
            print(f"The binary representation of {decimal_num} is {binary_result}.")
        except ValueError:
            print("Invalid decimal number.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
