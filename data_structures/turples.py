# Turples are light-weight collections used to keep track of related but different items
# Turples are immutable(The items in a turple cant change once it has been created)
# They are useful for containing a snapshot of data
# They guarantee some general security and reliability in the data
# Parenthesis are used to create a turple ();
# For a one item turple to be valid, a comma must be added at the end, otherwise, it gets resolved to a native type
nums = (3,)  # a one item turple

# A  turple can also be created by using turple(newTurple)
# A turple containing student info
student = ('Michael', 19, 'Engineering', 70)

# To unpack all values in a turple

name, age, course, points = student  # unpacks all values of the turple
print(
    f"The students name is {name}, their age is {age}. They take {course} and had {points} points in the last exam")
# To unpack and leave out some values in a turple

name, age, course, _ = student
print(
    f"The student name is {name}, they are {age} years and they take {course} ")

# .index(item) can be used to return the lowest index position of items in a turple

# values in a turple can be unpacked from a function that returns a turple


def http_Code():
    return 200, 'ok'


code, status = http_Code()  # Unpacks the turple returned from the function
print(f"The status code is {code} and the message is {status}")
