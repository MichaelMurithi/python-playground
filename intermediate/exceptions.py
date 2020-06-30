try:
    int('foo')
except ZeroDivisionError:
    print('Cant divide by zero')
except ValueError as e:
    print(f'Ooops an error occured: {e}')