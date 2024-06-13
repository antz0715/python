import time  # Import the time module to measure the typing speed

def typing_speed_test():
    # The sentence that the user needs to type
    test_sentence = "The quick brown fox jumps over the lazy dog."
    print("Typing Speed Test")
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter when you are ready to start...")

    start_time = time.time()  # Record the start time
    user_input = input("\nStart typing now:\n")  # Get the user's typed input
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate the time taken to type the sentence
    words_typed = len(user_input.split())  # Count the number of words typed
    words_per_minute = (words_typed / elapsed_time) * 60  # Calculate words per minute

    # Display the results
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Typing speed: {words_per_minute:.2f} words per minute")

    accuracy = calculate_accuracy(test_sentence, user_input)  # Calculate typing accuracy
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(reference_text, typed_text):
    reference_words = reference_text.split()  # Split the reference sentence into words
    typed_words = typed_text.split()  # Split the user's typed text into words
    
    correct_words = 0  # Initialize the count of correct words
    for ref_word, typed_word in zip(reference_words, typed_words):
        if ref_word == typed_word:  # Check if each word matches
            correct_words += 1  # Increase the count of correct words
    
    accuracy = (correct_words / len(reference_words)) * 100  # Calculate accuracy percentage
    return accuracy

if __name__ == "__main__":
    typing_speed_test()  # Call the function to start the typing speed test
