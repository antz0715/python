import random
# This line tells Python we want to use some special tools that let us do random things,
# like picking a mystery word randomly from a list.

# Here, we're creating a little box of magic (a function) 
# Its job is to pick one word out of a secret hat (a list of words) so you can guess it.
def choose_word():
    words = ['tiger', 'dinosaur', 'galaxy', 'volcano', 'balloon']
    return random.choice(words) # is like closing our eyes and picking one word from the list without looking

def play_game(secret_word):
    # This is where we set up the actual game. We tell it the mystery word, and it starts the guessing game.
    guessed_letters = ['_'] * len(secret_word) #  sets up a bunch of blanks 
    # on the screen, one for each letter in the mystery word. It's like the empty spots in a crossword puzzle waiting to be filled in.
    attempts = 10  # Or any number you see fit
    guessed = False

    print("Welcome to the Mystery Word Game!")
    print(" ".join(guessed_letters))

    while attempts > 0 and not guessed:
        # This part keeps the game going, letting you guess letters until you either get the word right or run out of attempts.
        guess = input("Guess a letter: ").lower() # asks you to guess a letter and makes sure that letter is in a simple, lowercase form no matter how you type it.

        if guess in secret_word: # If the letter you guessed is in the word 
            for index, letter in enumerate(secret_word): # reveals where that letter appears in the mystery word by replacing the blanks with the correct letter.
                if letter == guess:
                    guessed_letters[index] = guess
            print("Correct! " + " ".join(guessed_letters))
            #it reveals where that letter appears in the mystery word by replacing the blanks with the correct letter.
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.") 
            #If the letter is not in the word, you lose one of your attempts, and it tells you how many attempts you have left.

        if '_' not in guessed_letters:
            guessed = True #it means you've guessed the word correctly. 

    if guessed:
        print("Congratulations, you've guessed the word!") #The game congratulates you!
    else:
        print(f"Game over! The secret word was {secret_word}.")
        # if you run out of attempts before guessing the word, it tells you the game is over and reveals the mystery word.

if __name__ == "__main__":
    secret_word = choose_word()
    play_game(secret_word)

# This is like saying, "If I'm the main act (the script you're directly running), let's start the game." 
# It picks a mystery word with choose_word() and then starts the game with that word using play_game(secret_word)
    

# Function: Think of it like a little machine that does a specific job. You give it something (input), it does some magic, and then it gives something back (output).
    
# Loop: It's like a repeating cycle that keeps going until a certain condition is met. In this game, it's used to keep asking you for guesses.
    
# List: Imagine a list as a line of boxes, each containing something different. In this game, we use a list to keep track of the guessed letters.
    
# Variable: It's like a container or a label for storing information that can change as the program runs. For example, attempts is a variable that keeps track of how many guesses you have left