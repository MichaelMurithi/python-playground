# Dictionaries are mutable
# dictionary keys can only be of mutable types
# Dictionaries are used when there is a need to access additional data associated with a particular key
# Curly brackets {} are used to make an empty dictionary
# dict() method can also be used to create an empty dictionary
# The keys in a dictionary are not ordered

student = {'name': 'Myke', 'age': 30, 'course': 'Engineering'}
# accesses the 'course' attribute of the student dictionary
print(student['course'])

# .get(key) method takes in akey and returns value if it is available. It does not return an error when the value is not available

# .get() method can also take "default value" as the second parameter and retursn a default value when the value is not avilable

# to add values in a dictionary:
student['year'] = 1
# dict1.update(dict2) is used to coombine the elements of dict2 to dict1

student_details = {'nationality': 'Kenyan',
                   'location': 'Nairobi', 'status': 'single'}
student.update(student_details)
print(student)
# .keys() method in dictionaries returns a list of keys in a dictionary
print(student.keys())
# .values() method in a dictionary returns a list of values
print(student.values())
# .items() method returns a turple of items in a dictionary
print(student.items())
