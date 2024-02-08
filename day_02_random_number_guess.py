# Guess a random number
import random

# Greetings
user_name = input("What is your name? ")
print(f"""
    Hello {user_name}, let's play a game!

    I pick a number between 0-50, and you have 5 chances to guess.

    With each guess, I will confirm if you are getting closer.
""")

def guessing_game():
    guess_count = 0

    # Random Number Generator
    possible_numbers = range(0,50)
    random_number = random.choice(possible_numbers)

    # User input
    while guess_count < 5:
        user_guess = int(input("Guess a number: "))
        guess_count += 1
        if user_guess == random_number:
            print(f"You got it, {user_name}!")
            break
        elif user_guess < random_number:
            print("Higher...")
        elif user_guess > random_number:
            print("Lower...")
        else:
            break
    if guess_count == 5:
        print(f"Game over! The number was {random_number}")


guessing_game()










