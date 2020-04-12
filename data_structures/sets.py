# Are data types that allow storage of immutable data types uniquely
# Sets do not allow duplicate values
# A set does not have order
# It has a benefit of allowing very first membership testing
# Curly brackets are used to create sets {}
names = {'Myke', 'Max', 'Nina', 'Navin'}

# Since sets do not allow duplicate values, they can be used to sort out only unique values from a list
repeatedVals = ['April', 'August', 'March', 'January', 'April']
uniqueVals = set(repeatedVals)  # returns a set of unique values
print(uniqueVals)

# Sets do not surport indexing

# .add(item) is used to add values in a set
rainbow_colors = {'red', 'orange', 'Yellow',
                  'green', 'blue', 'Indigo', 'Violet'}
rainbow_colors.add('Indigo')
print(rainbow_colors)

# .discard() is used to remove items in a set whether they're present or not without complaining with an error
rainbow_colors.discard('Yellow')

# .remove() removes an item in a set and throws an error if the item is not present

rainbow_colors.remove('Violet')
print(rainbow_colors)

# .update() can be used to join two sets together. It expects a sequence
favourite_colors = {'Maroon', 'Purple', 'blue'}
rainbow_colors.update(favourite_colors)
print(rainbow_colors)

# Set Operations
# set1.union(set2) creates a new set with all the items from both set1 and set2
# .union() (|) does not include duplicate values
all_colors = rainbow_colors.union(favourite_colors)
print(rainbow_colors)

# set1.intersection(set2) (&) creates a new set containing only values that are in both sets
similar_colors = rainbow_colors.intersection(favourite_colors)
print(similar_colors)
# x.difference(y) creates a new set with items in x but not in y. (^)
unique_colors = rainbow_colors ^ favourite_colors

print(unique_colors)
h
