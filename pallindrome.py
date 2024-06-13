def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Remove spaces and convert to lowercase for uniform comparison
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

def main():
    user_input = input("Enter a string to check if it is a palindrome: ")
    
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
