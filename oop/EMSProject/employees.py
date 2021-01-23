import datetime
import calendar

'''
**** Employees package ****
'''

class Employee:
    '''
    Base class for all employees, defines the common features possesed by all employees.
    '''
    def __init__(self,id,name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee): #The salaried employeee inherits the Employee class
    '''
    Class of employees who receive a salary based on the number of days they work and their daily rate
    '''
    
    def __init__(self,id,name,rate_per_day):
        super().__init__(id,name)
        self.rate_per_day = rate_per_day

    def calculate_payroll(self):  
        today = datetime.datetime.now() #today's date
        totalDays = calendar.monthrange(today.year, today.month)[1] #Total days worked by the employee
        return self.rate_per_day * totalDays

class PartTimeEmployee(Employee):
    ''''
    Parttime employees who are payed based on the number they have worked and their hourly rate
    '''

    def __init__(self,id,name,total_hours,rate_per_hour): 
        super().__init__(id,name) #
        self.total_hours = total_hours
        self.rate_per_hour = rate_per_hour

    def calculate_payroll(self):
        return self.total_hours * self.rate_per_hour


class CommissionEmployee(SalaryEmployee):
    '''
    Commision based employees are salaried employees who wre offered a commision
    '''
    def __init__(self,id,name,rate_per_day,commision):
        super().__init__(id,name,rate_per_day)
        self.commision = commision

    def calculate_payroll(self):
        salary = super().calculate_payroll()
        return salary + self.commision


class Manager(SalaryEmployee):
    def work(self,hours):
        print(f"{self.name} is managing the project team for {hours} hours")


class Developer(SalaryEmployee):
    def work(self,hours):
        print(f"{self.name} is working on the project for {hours} hours")


class Salesman(CommissionEmployee):
    def work(self,hours):
        print(f"{self.name} as salesman is handling the client calls for {hours} hours")


class Worker(PartTimeEmployee):
    def work(self,hours):
        print(f"{self.name} as worker has completed his tasks in {hours} hours")

