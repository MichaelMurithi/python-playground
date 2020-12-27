class Employee:
    TotalEmployees = 0
    def __init__(self, empno, ename, salary, deptno):
        self.Empno = empno
        self.Ename = ename
        self.Salary = salary
        self.Deptno = deptno
        Employee.TotalEmployees += 1

    
    def showEmployee(self):
        print("Employee # :{} \n Employee Name : {}\n Salary : {}\n Department # : {}".format(self.Empno,self.Ename, self.Salary,self.Deptno))

emp1 = Employee(101, "Sekhar", 4500, 10)
emp2 = Employee(102, "Selina", 4600, 20)

emp1.showEmployee()
emp2.showEmployee()

print("Total Employees", Employee.TotalEmployees)