def main():
    print("I am inside the main function.\n")
    n1=int(input("Enter first number: "))
    n2=int(input("Enter second number: "))

    sum_one(n1,n2)
    min_one(n1,n2)
    max_one(n1,n2)

    print("\nBack to main function.")

def sum_one(x,y):
    sum = x + y
    print("Sum of", x, "and", y, "inside the \'find_sum\' function =", sum)

def min_one(a,b):
    if a<b:
        print("Smaller of", a, "and", b, "inside the \'find_min\' function =", a)
    else:
        print("Smaller of", a, "and", b, "inside the \'find_min\' function =", b)

def max_one(c,d):
    if c < d:
        print("Bigger of", c, "and", d, "inside the \'find_mix\' function =", d)
    else:
        print("Bigger of", c, "and", d, "inside the \'find_max\' function =", c)

main()