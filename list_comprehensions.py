# looping through and modifying each element in a list
# To return square numbers upto 10:
squares = [num * num for num in range(11)]
print(squares)

# To return a list of turples
names = ['Myke', 'Purity', 'Eric', 'Juliana']
names_details = [('Length', len(name))
                 for name in names]  # returns a list of turples
print(names_details)

# conditional statements can be added on the right side of a list comprehension
# To return only a list of even numbers between a given range

even_squares = [num * num for num in range(11) if num % 2 == 0]
print(even_squares)

# To convert the numbers into a comma separated string
string_squares =','.join([str(even_square) for even_square in even_squares])
print(string_squares)