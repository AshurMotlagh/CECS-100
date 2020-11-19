
filename = True
while filename:
    try:
        filename = input("\nEnter a file name: ")
        thefile = open(filename, 'r')
        inside = thefile.read()
        print("Here are the contents of the file,", filename)
        filename = False
        print(inside)

        thefile.close()

    except FileNotFoundError:
        print("File does not exist, try again. ")

print("\n\n")


def grosspay():
    h = hours()
    print("\n")
    p = payrate()
    print('\n')
    grosspay = h * p
    print("Your Gross pay is", grosspay)


def hours():
    result = True
    while result:
        try:
            hour = int(input("How many hours did you work? "))
            while hour <= 0:
                hour = int(input("Must be greater than or equal to zero, enter again: "))
            result = False
            return hour

        except ValueError:
            print("must be a number")


def payrate():
    result = True
    while result:
        try:
            pay = int(input("What is your pay rate? "))
            while pay < 0:
                pay = int(input("Must be greater than zero, enter again: "))
            result = False
            return pay

        except ValueError:
            print("must be a number")


grosspay()
