# use transform functions like sorted, filter, map


def isEven(num):
    return num % 2 == 0


def isLowerCase(char):
    return  char.islower()


def square(value):
    return value * value


def getGrade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 40:
        return 'D'
    return 'F'
        


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    scores = (81, 89, 94, 78, 61, 30, 99, 74)

    # : use filter to remove items from a list
    odds = list(filter(isEven, nums))
    print(odds)
    # : use filter on non-numeric sequence
    lowerCaseLetters = list(filter(isLowerCase, chars))
    print(lowerCaseLetters)
    # : use map to create a new sequence of values
    squares = map(square,nums)
    print(list(squares))
    # : use sorted and map to change numbers to grades
    sortedScores = reversed(sorted(scores))
    grades = list(map(getGrade, sortedScores))
    print(grades)
    

if __name__ == "__main__":
    main()
