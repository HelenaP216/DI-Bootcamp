
# Mini-Project - Tic Tac Toe

# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
#     Conditionals (if, elif, else)
#     Loops (for, while)
#     Functions
#     List manipulation
#     User input

# Key Python Topics:
#     Lists (2D lists)
#     Loops (while)
#     Conditional statements (if, elif, else)
#     Functions
#     User input (input())
#     String formatting

# 🛠️ What you will create
#       A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.

# Instructions:
#   Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’).
#   The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
#   If all squares are filled and no player has three in a row, the game is a tie.

# Step 1: Representing the Game Board
#     You’ll need a way to represent the 3x3 grid.
#     A list of lists (a 2D list) is a good choice.
#     Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

grid_line_1 = ["a ", "a ", "a "]
grid_line_2 = ["b ", "b ", "b "]
grid_line_3 = ["c ", "c ", "c "]

game_grid = [grid_line_1, grid_line_2, grid_line_3]
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in game_grid:
    for item in row:
        # Print each item followed by a tab, without a newline
        print(f"{item}\t", end='')
    # Print a newline character after each row is completed
    print()
# print(game_grid)

# Step 2: Displaying the Game Board
#     Create a function called display_board() to print the current state of the game board.
#     The output should visually represent the 3x3 grid.
#     Think about how to format the output to make it easy to read.

def display_board():
    line_1 = "Welcome to TIC TAC TOE!\n"
    line_2 = "TIC TAC TOE\n"
    line_3 = "*****************\n"
    line_4 = "*" + "     " + "|" + "   " + "|" + "     " + "*\n"
    line_5 = "*" + "  " + "---|---|---" + "  " + "*\n"
    line_6 = "*" + "     " + "|" + "   " + "|" + "     " + "*\n"
    line_7 = "*" + "  " + "---|---|---" + "  " + "*\n"
    line_8 = "*" + "     " + "|" + "   " + "|" + "     " + "*\n"
    line_9 = "*****************"
    board_frame = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7 + line_8 + line_9
    print(board_frame)

display_board()