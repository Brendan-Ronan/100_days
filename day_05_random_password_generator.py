# Random Password Generator

import random
import string

print("Hello, this is Brendan's DIY Random Password Generator made in Python\n")

# User input
length = int(input("How many characters: \n"))

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

random_password = generate_password(length)
print("Random Password: ", random_password)






