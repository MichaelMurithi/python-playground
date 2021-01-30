'''
In this code snippets, we try to understand the limitations of a 'is-a' relationship
 - For example, a square is a rectangle, hence we have a class Square that inherits the properties of a rectangle
 - However, this does not obey the 'Liskov Substitution Principle' since the square cannot substitute a rectangle.
 - An attempt to substitute a square for a rectangle leads to errors since the height and width properties are different for a square and a rectangle 
'''

class Rectangle:
    def __init__(self,width=0,height=0):
        self._width = width
        self._height = height

    def get_width(self):
        return self.width
    
    def set_width(self,value):
        self._width = value
    
    def get_height(self):
        return self.height 

    def set_height(self,value):
        self._height = value

    width = property(get_width,set_width)
    height = property(get_height,set_height)

class AreaCalculator:
    def calculateArea(self,rectangles):
        for rectangle in  rectangles:
            print(f'Area: {rectangle.width * rectangle.height}')

class Square(Rectangle):
    def get_width(self):
        return self._width
    def set_width(self, value): #In a square a change in width should automatically set the same value for height
        self._width = value
        self._height = value

    def get_height(self):
        return self._height
    def set_height(self, value): #A change in height should automatically set the same values for the width
        self._height = value
        self._width = value

    width = property(get_width,set_width)
    height = property(get_height,set_height)

sq = Square()
sq.width = 10
sq.height = 10

rect = Square() #Trying to substitute a square for a rectangle
rect.width = 20
rect.height = 30

shapes = [sq,rect]

calculator = AreaCalculator()
calculator.calculateArea(shapes)

'''
The area calculations results are 
sq = 100
rect = 900
Hence, the implementation does not obey the "Liskov's Substitution principle" since a Square sub-class cannot substitute a rectangle class. 
- This are the limitations of an 'is-a' relationship
'''