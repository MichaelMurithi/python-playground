name = 'Myke'

# syntax for defining a function


def welcome(name):
    print(f"Hello {name}! Welcome to python")


welcome(name)

# Defining a function that takes a keyword argument
def calculate_numbers(x, y, operation='add'):
    if operation == 'add':
        return print(f"The sum is {x+y}")
    elif operation == 'subtract':
        return print(f"The difference is {x-y}")

#calling a function
calculate_numbers(5, 4, operation='subtract')
