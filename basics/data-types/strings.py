#Strings are formed using single quotes
name = 'Michael'
#Strings formed using double quotes
country = "Slovakia"
#Accessing characters using index positions
print(f"First letter in country, {country[0]}")
#Last character using negative indexing
print(f"last letter in country {country[-1]}")
#Slicing secong to 5th letter
print(f"Second to 5th letter {country[1:5]}")
#6th to second last character
print(f"Sixth to second last character {country[5:-2]}")

"""[String properties]
    - Strings are immutable (The elements of a string cannot be changed)

"""
#---------------------------------------------------------------
# 1. The del keyword can be used to delete the string entirely
to_delete = "I want to delete this string"
print(to_delete)

# 2. Concatenation involves joining two or more strings into a single one
first_name = "Michael"
last_name = "Murithi"

full_name = first_name + last_name

print(f"My full name is {full_name}")
# Parenthesis are used to concatenate a string in different lines
greeting = (
    'Hello'
    'Learner'
)

# The * operator can be used to repeat a string for a given number of times
print(f"My name called trice is {first_name * 3}")


#We can iterate through a string using a for loop

#---------------Function to count the number of times a letter appers in a string-------------------------
def count_letter(string,letter_to_count):
    count = 0
    for letter in string:
        if (letter == letter_to_count):
            count+=1
    return count

my_string = "Hey, Little birds like eating cool stuff"

print(f"Letter 't' appears in the string {count_letter(my_string,'t')} times")

#String membership test
'''
- We can test if a substring exists within a string or not using the in Keyword
'''

def search(substring, string):
    return substring in string #The in keyword is used for string membership test

print(search('cool',my_string))

#String built in functions
"""
- The 'enumerate function returns an enumerate object. It contains the index and value of all the items in the string as pairs
- 'len' returns the number of characters of the string
 """

list_enumerate = list(enumerate(my_string))
print('List(enumerate(my_string))',list_enumerate)

