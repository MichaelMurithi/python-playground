
class Point:
   
    def __init__(self,x,y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "({0},{1})".format(self.X,self.Y)

    def __add__(self,other): #defining the adition operatioin as part of operator overloading
        x = self.X + other.X
        y = self.Y + other.Y
        return Point(x,y)

    def __lt__(self,other): # overloading the less than operator
        p1 = self.X + self.Y
        p2 = other.X + other.Y
        return p1 < p2 
    

p1 = Point(10,20)
p2 = Point(5,10)

result = p1 + p2
print(result)

flag = p1 < p2
print("Is point p1 lesser than p2 ?", flag)