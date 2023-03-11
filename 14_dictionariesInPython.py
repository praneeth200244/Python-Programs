dic = {
    "A": "A",
    "B": "Boy",
    "C": "Can",
    "D": "Do",
    "E": "Everything",
    "F": "For",
    "G": "Girl",
    100: "Police",
    108: "Ambulance"
}

s = {}  # Empty dictionary
s = {1098: "Children help line", 101: "Fire station"}

# Accessing members of a dictionary
print(dic)
print(dic["B"])  # Raises error if key is not present in the dictionary
# Doesn't raise error if key is not present in the dictionary(prints None)
print(dic.get('B'))

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])
    print(f"The value corresponding to the key {key} is {dic[key]}")

print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")

dic.update(s)
print(dic)

s.clear()
print(s)

del s
del dic[100]
print(dic)

print(dic.pop(101))

print(dic.popitem())
