x = True
while x:
    try:
        x = int(input("Enter a number: "))
        print("Number is", x)
        x = False
    except ValueError:
        print("Enter an Integer")

print("\n \n ")

result = True
while result:
    try:
        n = int(input("Enter numo: "))
        d = int(input("Enter demo: "))
        result = n/d
        print("result =", result)
        result = False
    except ZeroDivisionError:
        print("Error, you cant divide a number by 0")
    except ValueError:
        print("Enter an Integer")

