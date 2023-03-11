# Required arguments(here a and b)
def averageR(a, b):
    print("Average=", (a+b)/2)


averageR(10, 15)
print()


# Default arguments
def averageD(a=6, b=4):
    print("Average=", (a+b)/2)


averageD()
averageD(10)
averageD(b=20)
averageD(5, 35)
print()

# Keyword arguments(order of arguments in function call doesn't matters)


def averageK(a, b, c=2):
    print("Average=", (a+b+c)/2)


averageD(b=16, a=100)
averageR(b=16, a=100)
averageK(100, 200, 400)
averageK(100, 200)
print()

# Variable length arguments


def averageV(*numbers):  # Here, numbers is treated as tuple
    sum = 0
    for i in numbers:
        sum += i
    print("Average=", (sum)/len(numbers))


averageV(10, 25)
averageV(1, 2, 3, 4, 5)
averageV(100, 200, 300, 400)
averageV(50, 65, 74, 48, 95, 25, 152, 5632, 4458)


def name(**name):  # Here name is treated as dictionary
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Suresh", lname="Iyengar", fname="Bengaluru")
