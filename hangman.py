import random

def hangman():
    words = ["python", "java", "swift", "javascript"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Let's play Hangman!")

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(display_word)
        
        if "_" not in display_word:
            print("Congratulations! You guessed the word.")
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
        
        if attempts == 0:
            print(f"Game over! The word was: {word}")

hangman()
