# Rock Paper Scissors
import random

print("Hello, lets play Rock Paper Scissors!")
name = input("What is your name? ")

def rock_paper():
    user_wins = 0
    cpu_wins = 0

    while user_wins < 3 and cpu_wins < 3:
        ### User input
        moves = ["Rock", "Paper", "Scissors"]
        user_move = input(f"Enter your move, {name}: ")

        ### Validate user input
        while user_move not in moves:
            print("Enter a valid move ")
            user_move = input(f"Enter your move, {name}: ")

        ### Random CPU move generator
        cpu_move = random.choice(moves)
        print(f"Computer Move: {cpu_move}")

        ### Move comparison
        if cpu_move == user_move:
            print("Tie!")
        elif (cpu_move == 'Rock' and user_move == 'Scissors') or \
            (cpu_move == 'Scissors' and user_move == 'Paper') or \
            (cpu_move == 'Paper' and user_move == 'Rock'):
            cpu_wins += 1
            print(f"""Computer wins!
            Score
            Computer: {cpu_wins}
            User: {user_wins}
            """)
        else:
            user_wins += 1
            print(f"""{name} wins!
            Score
            Computer: {cpu_wins}
            User: {user_wins}
            """)

    if user_wins == 3:
        print(f"{name} wins the game!")
    else:
        print("Computer wins the game!")

### Call the funcrtion
rock_paper()
