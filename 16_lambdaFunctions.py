# Function definition
# def multiply(x) :
#     return (2*x)

# Equivalent Lambda function
def multiply(x): return (2*x)


def average(x, y, z): return (x+y+z)/2


print(multiply(5))
print(average(1, 2, 3))

# Passing function as a parameter


def apply(fx, value):
    return (6 + fx(value))


print(apply(multiply, 2))
print(apply(lambda x: (2*x), 2))
print(apply(lambda x: (2*x*x), 2))
