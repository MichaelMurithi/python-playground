# A comprehention on a set

square_set = {num*num for num in range(6)}
print(square_set)

# to create a dictionary comprehension from a list comprehension:

# creates a dictionarycomprehension
square_dict = {num: num * num for num in range(6)}
print(square_dict)
