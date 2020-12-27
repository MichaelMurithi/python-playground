class Father:
    
    def FatherProperty(self):
        print(" __Rich Father's Property ***")


class Mother:

    def MotherProperty(self):
        print(" __Rich Mother's Property ***")


class Child(Father, Mother): #The child class Inherits properties of 2 parent/base classes

    def Property(self):
        print("Child will inherit : **_**")
        super().FatherProperty() #Accessing the methods from the first parent class
        super().MotherProperty() #Accessing the methods of the second parents class
        print("****And the child is very rich***** and happy  :)*** ")

child1 = Child()
child1.Property()