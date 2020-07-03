# The .split(separator) can be used to split a string into a list using the given separator

my_data = "This is a space separated string"
data_list = my_data.split(" ")
print(data_list)

# The split can help unpack data
student = "Mary,18,Computer Science"
name, age, course = student.split(",")
print(
    f"The student name is {name} and their age is {age}. She pursues {course}")
# .join() method is used to join split parts using a specified separator
joined = " ".join(data_list)  # Joins the separated string
print(joined)

# when a set is passed in sorted method, a sorted list is returned
