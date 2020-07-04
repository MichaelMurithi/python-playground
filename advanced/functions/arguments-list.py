# Demonstrate the use of variable argument lists


# : define a function that takes variable arguments
def addition(*args):
    result = 0
    for num in args:
        result += num
    return result


def main():
    # : pass different arguments
    print(addition(1,2,3,4,5))

    # : pass an existing list
    myNums = [12,1,32]
    print(addition(*myNums))

if __name__ == "__main__":
    main()
