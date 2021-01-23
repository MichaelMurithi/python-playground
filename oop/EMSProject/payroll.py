'''
Payroll interface of  the employees management system
'''
class PayrollManagementSystem:
    '''
    An interface for all employees
    '''

    def calculate_payroll(self,employees):
        print("***Welcome to the Payroll Section ***")
        print("====================================")
        print("*****Payroll List****")

        for employee in employees:
            print(f"Employee #: {employee.id}\n Employee name :{employee.name}")
            print(f"Amount: {employee.calculate_payroll()}")
            print("--------------------------------------------")
