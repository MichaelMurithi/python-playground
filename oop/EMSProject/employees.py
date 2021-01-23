from payroll import SalaryPolicy, CommissionPolicy, PartTimePolicy
from employeemanagement import ManagerRole, DeveloperRole, SalesRole, WorkerRole

class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Manager(Employee,ManagerRole,SalaryPolicy):
    def __init__(self,id,name,rate_per_day):
        SalaryPolicy.__init__(self,rate_per_day)
        super().__init__(id,name)

class Developer(Employee,DeveloperRole,SalaryPolicy):
    def __init__(self,id,name,rate_per_day):
        SalaryPolicy.__init__(self,rate_per_day)
        super().__init__(id,name)


class Salesman(Employee,SalesRole,CommissionPolicy):
    def __init__(self,id,name,rate_per_day,commission):
        CommissionPolicy.__init__(self,rate_per_day,commission)
        super().__init__(id,name)


class Worker(Employee,WorkerRole,PartTimePolicy):
    def __init__(self,id,name,total_hours,rate_per_hour):
        PartTimePolicy.__init__(self,total_hours,rate_per_hour)
        super().__init__(id,name)


class Consultant(Employee,DeveloperRole,PartTimePolicy):
    def __init__(self,id,name,total_hours,rate_per_hour):
        PartTimePolicy.__init__(self,total_hours,rate_per_hour)
        super().__init__(id,name)
