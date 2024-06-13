import time

def set_timer(minutes, seconds):
    """
    Set a timer for the specified minutes and seconds.
    
    Parameters:
    minutes (int): The number of minutes for the timer.
    seconds (int): The number of seconds for the timer.
    """
    # Convert the total time into seconds
    total_seconds = minutes * 60 + seconds
    print(f"Timer set for {minutes} minutes and {seconds} seconds. Waiting...")
    
    # Loop until the timer reaches zero
    while total_seconds > 0:
        # Calculate the current minutes and seconds from the total seconds
        mins, secs = divmod(total_seconds, 60)
        # Format the time as MM:SS
        timeformat = f'{mins:02d}:{secs:02d}'
        # Print the current time on the same line
        print(timeformat, end='\r')
        # Wait for one second
        time.sleep(1)
        # Decrease the total time by one second
        total_seconds -= 1
    
    # Print the message when the timer is up
    print("Time's up! Time to wake up!")

def main():
    """
    Main function to run the timer.
    
    Prompts the user to enter the number of minutes and seconds for the timer
    and then starts the timer.
    """
    # Get the number of minutes from the user
    minutes = int(input("Enter the number of minutes: "))
    # Get the number of seconds from the user
    seconds = int(input("Enter the number of seconds: "))
    
    # Call the set_timer function with the user input
    set_timer(minutes, seconds)

# Execute the main function if the script is run directly
main()