import random

def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    print("I've picked a number between 1 and 100. Try to guess it!")

    while True:
        # Get user's guess and handle non-integer inputs
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Provide feedback based on the guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number correctly.")
            break

guess_the_number()  
