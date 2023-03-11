s = {}
print(type(s))

# Declaring empty set
s = set()
print(type(s))

# Duplicates are ignored by interpreter
s_1 = {2, 4, 6, 2}
s_2 = {2, 6, 10, 15, 25}
print(s_1)
print(s_2)
print(s_1, s_2)

# Accessing values in a set
for value in s_1:
    print(value, end=' ')
print()

# Set methods
print(s_1.union(s_2))
print(s_1.intersection(s_2))
print(s_1.isdisjoint(s_2))
print(s_1.issubset(s_2))

if 2 in s_2:
    print(2, "is found")
else:
    print(2, " is not found")

s_1.update(s_2)
print(s_1)

s_1.intersection_update(s_2)
print(s_1)

print(s_1.symmetric_difference(s_2))
s_1.symmetric_difference_update(s_2)
print(s_1)

s_1.add(256)
s_1.add(255)
print(s_1)

s_1.remove(255)
print(s_1)
s_1.discard(254)  # Doen't raise an error
print(s_1)

# To remove last element of the set
print(s_1.pop())

# To delete entire set itself
del s_2

# TO delete all items from the set
s_1.clear()
print(s_1)
