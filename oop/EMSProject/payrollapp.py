import payroll

salariedEmp = payroll.SalaryEmployee(101,'Sekhar',1000)
partimeEmp = payroll.PartTimeEmployee(102,'Michael',40,500)
commisionEmp = payroll.CommissionEmployee(103,'Maryam',1000,1500)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll([salariedEmp,partimeEmp,commisionEmp])
