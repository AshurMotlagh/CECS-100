def main():
    n1=int(input("Enter your first number: "))
    n2=int(input("Enter your second number: "))
    print()

    print("Calling method \"sum_two\" inside main function")
    s=sum_two(n1, n2)
    print("Sum of ", n1, "and", n2, "inside \'main\' function is: ", s)
    print()

    print("Calling method \"min_two\" inside main function")
    minimum=min_two(n1, n2)
    print("Minimum of", n1, "and", n2, "inside \'main\' function is: ", minimum)
    print()

    print("Calling method \"max_two\" inside the main function")
    maximum=max_two(n1, n2)
    print("Maximum of", n1, "and", n2, "inside \'main\' function is: ", maximum)
    print()

    average=find_average(n1, n2)
    print("Average of ", n1, "and", n2, "inside \'main\' function is: ", average)

    find_range=maximum-minimum
    print("Value of Range inside main function is: ", find_range)

def sum_two(a, b):
    sum =a+b
    return sum

def min_two(c, d):
    mi = min(c, d)
    return mi

def max_two(e, f): #this is another way to do it with if else.
    if e>f:
        ma=e
    else:
        ma=f
    return ma

def find_average(g, h):
    average=(g+h)/2
    return average


main()
