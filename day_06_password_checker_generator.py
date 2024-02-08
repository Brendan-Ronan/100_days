import random
import string


def get_user_choice():
    # User choice
    while True:
        try:
            choice = int(input("Choose an option: \n" \
                "1: Create password\n" \
                "2: Generate random password\n"))
            if choice in [1, 2]:
                break
            else:
                print("Invalid entry. Enter 1 or 2.")
        except ValueError:
            print("Invalid entry. Enter 1 or 2.")

    return choice

def create_user_password():
    # User creates their password
    password = input("Enter your password: ")
    confirm = input("Confirm password: ")
        
    while password != confirm:
        print("Passwords do not match. Try again.")
        password = input("Enter your password: ")
        confirm = input("Confirm password: ")
        
    print(f"Your password: {password}")
    check_strength(password)
    
def check_strength(password):
    # Check user's password strength
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)
    is_long = len(password) >= 10

    criteria = {
        'has_uppercase': has_uppercase,
        'has_lowercase': has_lowercase, 
        'has_special': has_special,
        'is_long': is_long
    }

    strength_count = sum(criteria.values())

    if strength_count == 1:
        print("Password is weak. Improve by adding complexity.")
    elif strength_count == 2:
        print("Password is moderately strong. Consider additional improvements.")
    elif strength_count == 3:
        print("Password is strong.")
    else:
        print("Password is very strong. Great job!")

def generate_random_password():          
    # Generate a random password
    length = int(input("How many characters: \n"))
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Random Password: {random_password}")

def create_password():
    # Main function to handle user's password creation or random password generation
    choice = get_user_choice()

    if choice == 1:
        create_user_password()
    elif choice == 2:
        generate_random_password()
    else:
        print("Invalid entry. Try again")

# Run the program
create_password()





