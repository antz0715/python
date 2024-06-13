import random

def magic_8_ball():
    # List of possible responses (reduced to 10)
    responses = [
        "It is certain.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Reply hazy, try again.",
        "Don't count on it.",
        "My reply is no.",
        "Outlook not so good.",
        "Very doubtful."

    ]

    while True:
        # Prompt the user to ask a question
        question = input("Ask the Magic 8 Ball a question (or type 'quit' to exit): ")
        
        if question.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Select a random response
        answer = random.choice(responses)
        
        # Display the response
        print("Magic 8 Ball says: " + answer)

magic_8_ball()
