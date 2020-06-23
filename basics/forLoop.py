rainbow_colors = ['Red', 'Orange', 'Yellow', 'Green', 'Violet']

for color in rainbow_colors:  # loops through the list and prints every element in the list
    print(color)

# looping through a range of elements


def isEven(num):
    return num % 2 == 0


nums = []
# returns a list of numbers between 0 and 11
for num in range(0, 11):
    nums.append(num)
print(nums)


# looping through keys in an object
student = {'name': 'Myke', 'age': 19, 'course': 'Computer Engineering'}

for key in student.keys():
    print(key)

# to loop through an object as a list of turples

for key, value in student.items():
    print(key, value)

# enumerate(list) is a funtion that returns a turole containing list items and their index
for i, color in enumerate(rainbow_colors):
    print(f"index: {i}: color: {color} ")
