from abc import ABC, abstractmethod #the ABC class and absractmethod decorator are required to implement an abstract class

class Institute:
   
    def __init__(self):
        print(type(self).__name__," details :")

    def coursesOffered(self): #default classes offered at an institute
        print("Courses Offered : C, C++, Java, .NET")

    @abstractmethod #decorator used to define an abstract method
    def address(self) : pass #Address method is abstract since each institute has a different institute


class TechnoAcademy(Institute):
    
    def coursesOffered(self): #overides the courses offered method
        print("Courses Offered : Python, Data Science, Xamarin") 

    def address(self): #implements the 'address' abstract method
        print("Email : technoacademy@gmail.com \nCity : Bratislava \nStreeet : Stare Grunty 35")


ta = TechnoAcademy()
ta.address()