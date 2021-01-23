import payroll,employees,employeemanagement

# salariedEmp = employees.SalaryEmployee(101,'Sekhar',1000) #creates an instance of a salaried employee
# partimeEmp = employees.PartTimeEmployee(102,'Michael',40,500) #creates an instance of a part time employee
# commisionEmp = employees.CommissionEmployee(103,'Maryam',1000,1500) #creates an instance of a commision based employee

manager = employees.Manager(101,'Sekhar',1000)
developer = employees.Developer(102,'Michael',2500) 
salesman = employees.Salesman(103,'Maryam',1000,1500) 
cleaner = employees.Worker(103,'Wafula',10,250) 

employees = [manager,developer,salesman,cleaner]

ems = employeemanagement.PerfomanceManager()
ems.track(employees,40)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll(employees)

