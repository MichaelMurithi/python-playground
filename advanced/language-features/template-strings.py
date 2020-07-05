# practice template string functions
from string import Template

def main():
    # Usual string formatting with format()
    string1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(string1)
    
    # TODO: create a template with placeholders
    template1 = Template('I am watching ${course} by ${instructor}')
    # TODO: use the substitute method with keyword arguments
    string2 = template1.substitute(course="Advanced Python", instructor="Joe Miriami")
    print(string2)
    # TODO: use the substitute method with a dictionary
    courseDetails = {
        "course":"Advanced Python",
        "instructor":"Joe Marini"
    }
    string3 = template1.substitute(courseDetails)
    print(string3)
    
if __name__ == "__main__":
    main()
    