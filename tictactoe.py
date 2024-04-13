def print_board(board):
    for row in board: # loop goes through each row in the board.
        print(" | ".join(row)) # joins each element in the row with a | to look like a Tic-Tac-Toe board.
        print("-" * 9) #  prints a line after each row to separate them visually.

def check_win(board, player): # It creates a list of all possible win conditions (rows, columns, diagonals).
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions 
#  it checks if any of these conditions are met with the current player's marks 
# (player, player, player). 
# If yes, the player wins.

def get_player_move():
    while True:
        try:
            # It asks the player to enter a position (1-9). 
            # If the input is not a number or is outside the range, it keeps asking
            position = int(input("Enter position (1-9): ")) - 1
            if position in range(0, 9):
                return position
            else:
                print("Invalid position. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# This updates the board with the player's move.
def update_board(board, position, player):
    # It calculates which row and column the position corresponds to.
    row = position // 3 # 5 // 3, which equals 1. So, position 6 is in the second row (row 1, since we start counting from 0).
    col = position % 3 #5 % 3, which equals 2. So, position 6 is in the third column (column 2, since we start counting from 0).
    if board[row][col] == " ":
        board[row][col] = player
        return True #If the chosen spot is empty (" "), it places the player's mark (X or O) there and returns True.
    else:
        return False # If the spot is taken, it returns False, and the player has to choose again.


# The main function where the game runs.
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    # It sets up an empty board and starts with player X

    for _ in range(9):
        print_board(board)
        print(f"Player {player}'s turn.")
        
        position = get_player_move()
        if update_board(board, position, player):
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!") #checks for a win 
                return
            player = "O" if player == "X" else "X"
        else:
            print("That position is already taken.")
    
    print_board(board)
    print("It's a tie!") #checks for a tie

if __name__ == "__main__":
    main()
