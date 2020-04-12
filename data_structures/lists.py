# Lists are created using square brackets
# A list can also be declared by using list();
# A comma is used to separate the items in a list
# A list can contain duplicate values
# A list is mutable, the elements in a list can be changed
names = ['Myke', 'Cathreen', 'Purity', 'Doris']

for name in names:  # Prints all the elements in a list
    print(name)

# lists retain the order of items in them
# Values in a list can be updated
# len(list) is used to get the number of items in a list

print(len(names))  # prints the number of elements in a list
# Sorting Lists

lottery_numbers = [11, 2, 3334, 23, 122, 33344, 7665]

# sorted can be used to sort lists. It takes the list, and an optional boolean argument reverse
sortedNums = sorted(lottery_numbers, reverse=True)
print(sortedNums)

# .sort() method can be used to sort data in a list in ascending order. It does not make a copy of the list
lottery_numbers.sort()
print(lottery_numbers)

# .reverse() method can be used to sort data in a list in descending order
lottery_numbers.reverse()
print(lottery_numbers)

# .append() method is used to add a value to a list
lottery_numbers.append(90)
print(lottery_numbers)
# .insert() method is used to insert a value into a list at a specified position
# it takes two arguments, the position and the value

lottery_numbers.insert(4, 50)
print(lottery_numbers)

# .extend(anotherList) is used to join two lists together
names1 = ['Peter', 'Emmanuel', 'Eric']
names.extend(names1)
print(names)

# 'in' can be used to check whether a value exists in a list or not. It returns True/False
# Returns False since the list of names does not include 'Rose'
print('Rose' in names)

# .index(item) can be used to check and return the first index appearance of an item in a list.
# it takes the object to be looked for as the argument
names.index('Peter')

# .count(item) is used to count the number of times an item occurs in a list. Takes the item as an argument.
names.count('Myke')

# to change values at a specific position:
names[2] = 'Lindah'
# .remove(item) removes the first occurence of an item in a list
names.remove('Eric')
# .pop() removes the last item in a list and returns the removed item
# it can take the number of items to be removed from the list as the argument
names.pop()

# to slice an element in a list
first_three = names[0:3]
print(first_three)  # slices the first 3 names
from_three = names[3:]  # slices the list from index position 3 to the end
print(from_three)
