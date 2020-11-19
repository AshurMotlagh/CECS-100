ans="yes"
while ans == "yes" or ans == "YES" or ans == "Yes" or ans == "Y" or ans == "y":
    fac = int(input("\nEnter a positive number, I will tell you the factorial of that number: "))
    fact = fac
    total = 1
    for n in range(1, fac+1):
        total = total*n
    print("\nFactorial of", fac, "using \"for loop\"", total)
    total = 1
    while fact > 0:
        total = total * fact
        fact = fact-1
    print("Factorial of", fac, "using \"while loop\"", total)
    ans = str(input("\nDo you want to find out more? "))
print("Thanks for using this program!")
