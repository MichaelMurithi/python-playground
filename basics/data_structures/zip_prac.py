# a zip function takes two lists and returns turples
# To convert two lists into a list of turple:
names = ['Myke', 'Hannah', 'Philip', 'William']
scores = [10, 20, 90, 70]
details = zip(names, scores)  # returns a zip object
print(list(details))  # a list of turples

# to create a dictionary:
students_dict = dict(details)
print(dict(zip(names, scores)))  # creates a dictionary from a zip
