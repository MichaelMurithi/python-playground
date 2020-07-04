# Practice the usage of namdtuple objects

from collections import  namedtuple


def main():
    # TODO: create a Point namedtuple
    Points = namedtuple('Points', 'x y')
    point1 = Points(3,5)
    print(point1)
    # TODO: use _replace to create a new instance
    point2 = point1._replace(x = 9)
    print(point2)
    


if __name__ == "__main__":
    main()
