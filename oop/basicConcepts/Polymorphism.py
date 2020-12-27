'''
- Polymorphism refers to whenever an entity can change behaviour based on the arguments supplied to it.
It can been implemented using:
- Method overloading
- Method overriding
- Polymorphism with functions
- Operator overloading
'''
# Polymorphism with Functions - the ability in object oriented programming to use a common interface for multiple form data types

class English:
    def greet(self,name):
        print("Good morning ",name)


class Slovak:
    def greet(self,name):
        print("Dobry den ", name )

def greetings(language,name):
    language.greet(name)

english = English()
slovak = Slovak()

greetings(english,"Michael Kariuki")
greetings(slovak,"Michael Kariuki")
