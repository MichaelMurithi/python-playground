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

#sum() funtion is inbuilt to take a list and return the sum of sll elements in the list
#min() funtion takes a list of integers and returns the minimum value
# max() takes a list of integers and returns the maximum value

#function to take a coma separated string of numbers and return its sum
num_string = "4, 5, 10, 70, 12"
def sum_of_string(num_string):
    nums_str_list = num_string.split(", ")
    nums = [int(num) for num in nums_str_list]
    return sum(nums)

print(sum_of_string(num_string))