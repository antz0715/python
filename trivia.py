import random
#This line tells Python we want to use a set of functions that come with the "random" module.
# The "random" module includes tools for generating random numbers, 
# which we'll use to shuffle our flashcards so they appear in a different order each time.


# Flashcard data: questions and answers
# Here, we're creating a dictionary called flashcards where each item has a question about animals 
#as its key and the answer as its value. Think of it like a real set of flashcards where one side has a
# question and the other has the answer.
flashcards = {
    "What animal is known as the King of the Jungle?": "lion",
    "What is the fastest land animal?": "cheetah",
    "Which animal is the largest mammal in the world?": "whale",
    "What kind of animal is the only mammal capable of true flight?": "bat",
    "Which animal can be seen on the Porsche logo?": "horse",
    "What is the tallest animal in the world?": "giraffe",
    "Which animal has the longest lifespan?": "greenland shark",
    "What animal is known to have a memory span of three years?": "goldfish",
    "Which animal never sleeps?": "bullfrog",
}


# This line starts the definition of a function named quiz. 
# Functions are like mini-programs within our larger program that can be run whenever we call them. 
# This particular function takes one input, flashcards, which is our dictionary of questions and answers.

def quiz(flashcards):
    score = 0 #keep track of how many questions the player answers correctly. It starts at 0 because the player hasn't answered any questions yet.
    # This line creates a list of all the questions in our flashcards. \/
    questions = list(flashcards.keys()) # .keys() part gets all the questions from the flashcards dictionary, and list() turns them into a list so we can shuffle them around.
    random.shuffle(questions) # mixes up our list of questions so that each time you play the game, the questions come in a different order. It makes the game more fun and less predictable.
    
    for question in questions: #starts a loop that goes through each question in our shuffled list
        print(question) #Shows the current question to the player.
        answer = input("Your answer: ").lower().strip()
        #Asks the player for their answer, makes it lowercase (so it's not case-sensitive), 
        #and removes any extra spaces from the beginning or end.
        if answer == flashcards[question].lower():
            # checks if the player's answer is correct and updates their score accordingly.
            # It then tells the player if they were right or wrong.
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {flashcards[question]}.")
        print()
    
    print(f"Quiz finished! Your score is {score}/{len(flashcards)}.")
    #After all the questions have been asked, this line tells the player the game is over and shows their final score.
    # The len(flashcards) part tells us how many questions there were in total

if __name__ == "__main__":
    quiz(flashcards)

# This special line checks if this Python file is the main program being run.
# If it is, it calls the quiz(flashcards) function to start the game. 
# This is like the "start" button for our game.