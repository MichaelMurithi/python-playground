# defaultdict takes a factory method and returns a default value for a key which is not available in a list

# Demonstrate the usage of defaultdict objects

from collections import defaultdict

def getDefaultValue():
    return 0

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(getDefaultValue) #will use inbuilt integer function to assign default values 
        
    
    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
