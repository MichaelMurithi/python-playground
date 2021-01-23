import payroll

salariedEmp = payroll.SalaryEmployee(101,'Sekhar',1000) #creates an instance of a salaried employee
partimeEmp = payroll.PartTimeEmployee(102,'Michael',40,500) #creates an instance of a part time employee
commisionEmp = payroll.CommissionEmployee(103,'Maryam',1000,1500) #creates an instance of a commision based employee

payroll_system = payroll.PayrollManagementSystem() # Create an instance of the payroll system
payroll_system.calculate_payroll([salariedEmp,partimeEmp,commisionEmp]) #calculates the payroll of the employees instances
