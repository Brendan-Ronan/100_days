# Main function
def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)

# Introduces the rules
def intro():
    user_name = input("Enter a username: ")
    print(f"Hello, {user_name}! Let's play Tic Tac Toe!")
    print("\n")
    print("Rules: the objective is to align three of your marks (either X or O) "
          "horizontally, vertically, or diagonally on a 3x3 grid. "
          "Players take turns placing their marks on empty spaces, and the "
          "first to achieve a complete line wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")

# Blank playboard
def create_grid():
    print("Here is the playboard:  ")
    board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    return board

# Decides the players' symbols
def sym():
    symbol_1 = input("Player 1, choose to be X or O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are O. ")
    else:
        symbol_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("\n")
    return (symbol_1, symbol_2)

# Start the game
def start_game(board, symbol_1, symbol_2, count):

    # Decides the turn
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player "+ player + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column: enter 2]"))

    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column: enter 2]"))

    # Check if the square is already filled
    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column: enter 2]"))

    # Locate's player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1
    else:
        board[row][column] = symbol_2

    return (board)

# Check if the board is full
def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    while count < 10 and winner == True:
        gaming = start_game(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)

        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ")

        # Check for a winer
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")

    report(count, winner, symbol_1, symbol_2)

# Tells player if selection is out of range
def outOfBoard(row, column):
    print("Out of boarder. Pick another one. ")

# Prints the board nice!
def printPretty(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

# Checks if any winner is winning
def isWinner(board, symbol_1, symbol_2, count):
    winner = True
    # check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    # check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_2 + ", you won!")

        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    # check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")
    elif  board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner

def illegal(board, symbol_1, symbol_2, row, column):
    print("The square you picked is already filled. Pick another!")

def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")

# Call main
main()












