# deque objects are like double-ended queues

from collections import deque
import string


def main():
    # TODO: initialize a deque with lowercase letters
    deq = deque(string.ascii_lowercase)
    # TODO: deques support the len() function
    print(f'The are {len(deq)} letters')
    # TODO: deques can be iterated over
    for letter in deq:
        print (letter.upper(),end=",")
    # TODO: manipulate items from either end
    deq.pop()
    deq.append(2)
    deq.popleft()
    deq.appendleft(1)
    print(deq)
    # TODO: rotate the deque
    deq.rotate(-2)
    print(deq)


if __name__ == "__main__":
    main()
