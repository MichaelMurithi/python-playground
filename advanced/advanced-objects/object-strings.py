# customize string representations of objects


class Person():
    def __init__(self):
        self.firstName = "Joe"
        self.lastName = "Marini"
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person firstName:{self.firstName} lastName:{self.lastName}"
    # TODO: use str for a more human-readable string
    def __str__(self):
        return f"First Name: {self.firstName} Last Name: {self.lastName} age: {self.age}" 

def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))


if __name__ == "__main__":
    main()
