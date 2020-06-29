
class student:
    def __init__(self, **kwargs):
      self.name = kwargs['name']
      self.age = kwargs['age']
      self.year_of_study = kwargs['year']

    def print_student_details(self):
        print(f'Student Name:{self.name}\nAge: {self.age} \nYear: {self.year_of_study}')

student1 = student(name="Myke", age=30, year=3)
student1.print_student_details()