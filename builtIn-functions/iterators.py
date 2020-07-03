# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # : use iter to create an iterator over a collection
    iterDays = iter(days)
    print(next(iterDays))
    print(next(iterDays))

    # : iterate using a function and a sentinel
    with open("testfile.txt", "r") as file:
        lines = iter(file.readline, '')
        for line in lines:
            print(line)
    # : use regular interation over the days
    for index in range(len(days)):
        print(index+1,days[index])
    #  using enumerate reduces code and provides a counter
    for index, day in enumerate(days,start=1):
        print(index, day)
    # : use zip to combine sequences
    for index,dayNames in enumerate(zip(days, daysFr), start=1):
        print(index,dayNames[0], 'is', dayNames[1], 'in French' )


if __name__ == "__main__":
    main()
