class Employee:
    TotalEmployees = 0

    def __init__(self,empno, ename, salary, deptno):
        self.Empno = empno
        self.Ename = ename
        self.Salary = salary
        self.Deptno = deptno
        Employee.TotalEmployees +=1

    def showEmployee(self):
        print("Employee # :{} \n Employee Name : {}\n Salary : {}\n Department # : {}".format(self.Empno,self.Ename, self.Salary,self.Deptno))


class Salesman(Employee):
    
    def __init__(self,empno,ename, salary,deptno,commision):
        self.__Commision = commision #specifies the values specific for the class
        super().__init__(empno,ename,salary,deptno) #calls the constructor of the base class

    def showEmployee(self): #overides the showEmployee method of the base class.
        super().showEmployee()
        print(f"Commision {self.__Commision}")
        

salesman1 = Salesman(101, "Duncan Wekulo",10000, "10", 5000)
salesman1.showEmployee()
