def decorator(fn):
    def mfn(*args, **kwargs):
        print("This function takes two numbers as input")
        fn(*args, **kwargs)
        print("Hers's the correct answer\n")
    return mfn


@decorator
def sum(a, b):
    print(a+b)


@decorator
def difference(a, b):
    print(a-b)


sum(5, 10)  # decorator(sum)(10, 5) commenting @decorator above the function definition sum
difference(10, 5)
