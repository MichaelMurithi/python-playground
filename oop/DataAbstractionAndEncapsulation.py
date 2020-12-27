class Product:

    def __init__(self):
        self.__ProductId = ""
        self.__ProductName = ""
        self.__Price = 0

    def setProduct(self, pid, pname, price):
        self.__ProductId = pid #private variables for data abstraction
        self.__ProductName = pname
        self.__Price = price
    
    def updateProduct(self,newPrice): #methods to operate on the data and enable encasulation
        self.__Price = newPrice

    def showProduct(self):
        print("Product ID : {}\nProduct Name : {}\nPrice {}".format(self.__ProductId, self.__ProductName, self.__Price))


tv = Product()
tv.setProduct("TV101","Smart Television", 5000)
tv.showProduct()
tv.updateProduct(18500)
tv.showProduct()