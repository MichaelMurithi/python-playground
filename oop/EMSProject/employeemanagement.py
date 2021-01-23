'''
An interface to manage employees performance
'''

class PerfomanceManager:
    def track(self,employees,hours):
        print("**** Tracking employees performance**** ")
        print("=================================")

        for employee in employees:
            employee.work(hours)
            print("------------------------------")