import random # going to get a dice from the store

def guess_the_number(): #use _ to make fake spaces # define a function so it could do something for us 
    targetNumber = random.randint(1, 100) # variable , a  random variable
    print("I've picked a number between 1 and 100. Try to guess it!") # let the user know what is going on and what to do

    while True: # run forever unless told otherwise
        try: # try something
            guess = int(input("Enter your guess "))
        except ValueError: # if what you tried is not correct, "catch" an error
            print("please enter a valid integer") # lets the user know what they did wrong
            continue

        if guess < targetNumber: # simple if statement < means less than
            print("Too low! try again") 
        elif guess > targetNumber: # > means greater than
            print("Too high! Try again")
        else: # else in this case means guess = targetNumber
            print("Congrats! you've guessed the number correctly")
            break # stop the while True

guess_the_number()

