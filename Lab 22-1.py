def main():
    print("Checking miltiple value returning functions")
    firstName, lastName = full_name()
    print("Welcome, ", firstName, lastName)

    print("\nLets check some Boolean returning functions.")
    num=int(input("Enter a number, I will tell you its's a multiple of 3 or not. "))
    if multiple_of_three(num):
        print(num, "is multiple of 3")
    else:
        print(num, "is NOT multiple of 3")

    print("\nNow checking some MATH Modules")
    number=int(input("Enter a number :"))
    import math
    print("Square root of ", number, "=", math.sqrt(number))
    print("Square of ", number, "=", pow(number, 2))
    print("value of math.pi=", math.pi)


def full_name():
    first=str(input("Enter your first name: "))
    last=str(input("Enter your last name: "))
    return first,last


def multiple_of_three(lol):
    if lol % 3 == 0:
        result = True
    else:
        result = False
    return result


main()
