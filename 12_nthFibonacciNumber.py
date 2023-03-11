def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter any non-negative number: "))
print(f"{n}th fibonacci number is {fibonacci(n)}")
