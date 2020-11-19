def main():
    n1 = int(input("Enter a number: "))
    print()
    print("Calling\'show_double\' function inside main function.")
    show_double(n1)
    print()
    print("Back to \'main\' function.")

def show_double(a):
    print("Double of",a,"inside \'show_double\' is:",a*2)

main()