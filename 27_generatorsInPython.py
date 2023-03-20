def myGenerator():
    for i in range(0, 5):
        yield i


gen = myGenerator()

print(next(gen))
print(next(myGenerator()))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen1 = myGenerator()
for i in gen1:
    print(i)
