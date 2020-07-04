# advanced iteration functions in the itertools package
import itertools

def isBigNum(num):
    return  num > 30


def main():
    # : cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    #Repeats the collection when exausted
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    # : use count to create a simple counter
    count1 = itertools.count(10,10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    # : accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    accumulated = itertools.accumulate(vals)
    print(list(accumulated))
    # : use chain to connect sequences together
    chained = itertools.chain(seq1, vals)
    print(list(chained))
    # : dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    
    
if __name__ == "__main__":
    main()
    