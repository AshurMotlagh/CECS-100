def main ():
    num = int(input("Enter a number: "))
    result = factorial_num(num)
    print("Factorial of", num, "=", result)


def factorial_num(x):
    total = 1
    for n in range(1, x + 1):
        total = total * n
    return total


main()