def calculate_average():
    while True:
        try:
            # Ask the user how many numbers they want to average
            count = int(input("How many numbers would you like to average? "))
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    total_sum = 0

    # Collect the numbers and sum them
    for i in range(count):
        while True:
            try:
                number = float(input(f"Enter number {i+1}: "))
                total_sum += number
                break
            except ValueError:
                print("Please enter a valid number.")

    # Calculate the average
    average = total_sum / count

    # Display the result
    print(f"The average of the entered numbers is: {average}")

calculate_average()  
