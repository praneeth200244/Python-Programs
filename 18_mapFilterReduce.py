# Map

from functools import reduce


def cube(x):
    return (x*x*x)


print(cube(2))

l = [1, 2, 3, 4, 5, 6, 7, 8]
newL = []
for item in l:
    newL.append(cube(item))
print(newL)

newL_2 = list(map(cube, l))
print(newL_2)

# Filter


def filter_function(x):
    return x > 4


newList = list(filter(filter_function, l))
print(newList)

newList = list(filter(lambda x: x > 6, l))
print(newList)

# Reduce

sum = reduce(lambda x, y: x+y, l)
print(sum)
