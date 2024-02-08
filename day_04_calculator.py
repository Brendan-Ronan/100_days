print("Hello, this is a DIY Calculator built by Brendan in Python")

# define the functions
def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        raise ValueError("Cannot divide by zero")
    return num_1 / num_2

# user input
try:
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    operation = int(input("Choose an operation: \n" \
                    "1 = Addition\n" \
                    "2 = Subtraction\n" \
                    "3 = Multiplication\n" \
                    "4 = Division\n"))

    # calculations
    if operation == 1:
        solution = add(num_1, num_2)
        print(f"{num_1} + {num_2} = {solution}")
    elif operation == 2:
        solution = subtract(num_1, num_2)
        print(f"{num_1} - {num_2} = {solution}")
    elif operation == 3:
        solution = multiply(num_1, num_2)
        print(f"{num_1} * {num_2} = {solution}")
    elif operation == 4:
        solution = divide(num_1, num_2)
        print(f"{num_1} / {num_2} = {solution}")
    else:
        print("Invalid input. Ensure you're entering numbers.")
except ValueError as e:
    print(f"Error: {e}. Please enter valid numeric values.")
except Exception as e:
    print(f"Unexpected error: {e}. Check your input.")
