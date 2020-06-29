def main():
    student = {'name':'Myke', 'age':19, 'career':'Programmer'}
    print_student_details(**student)
    print_students('Myke', 'James', 'Trevor', 'Ombija')

def print_students(*students):
    
    if len(students):
        for student in students:
            print(student)

    else: print('Oops, seems no student is available!')

def print_student_details(**details):

    if len(details):
        for detail in details:
            print(f'Students {detail} is {details[detail]}')
    else:
        print('Oops!, seems no student details are provided')


if __name__ == '__main__': main()