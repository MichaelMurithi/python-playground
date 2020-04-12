# A fuction check_buzz that returns various values depending on the divisibility of a number
def check_buzz(last):
    for num in range(0, last + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("Fiz Buzz")
        elif num % 3 == 0:
            print("Fiz")
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


check_buzz(100)  # calls check_buzz function
