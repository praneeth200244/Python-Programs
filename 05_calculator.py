a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter the operator: ")

match operator:
    case '+':
        print(a, "+", b, "=", (a+b))
    case '-':
        print(a, "-", b, "=", (a-b))
    case '*':
        print(a, "*", b, "=", (a*b))
    case '/':
        if (b != 0):
            print(a, "/", b, "=", (a/b))
        else:
            print("Denominator cannot be zero")
    case '%':
        print(a, "%", b, "=", (a % b))
    case '//':
        print(a, "//", b, "=", (a//b))
    case '**':
        print(a, "**", b, "=", (a**b))
    case _:
        print("Invalid operator")
        
