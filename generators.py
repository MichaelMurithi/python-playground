#Generators can make more efficeient implementation of a comprehension
#They provide for lazy implementation of comprehensions.

# a generator of square of numbers in a range

nums = set((num *num for num in range(11)))
print(nums)