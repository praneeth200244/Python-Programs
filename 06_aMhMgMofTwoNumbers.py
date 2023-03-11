def aMhMgM(a, b):
    arithmeticMean = (a + b)/2
    print("Arithmetic mean = ", arithmeticMean)
    geometricMean = (a*b)**(1/2)
    print("Geometric mean=", geometricMean)
    harmonicMean = 2/((1/a)+(1/b))
    print("Harmonic mean=", harmonicMean)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

aMhMgM(a, b)
