num1 = 5
num2 = 9
def find_sum():
    sum=num1+num2
    print("Sum of",num1,"and",num2,"inside the \'find_sum\' function =",sum)

def find_min():
    if num1<num2:
        print("Smaller of", num1, "and", num2, "inside the \'find_min\' function =", num1)
    else:
        print("Smaller of", num1, "and", num2, "inside the \'find_min\' function =", num2)

def find_max():
    if num1<num2:
        print("Bigger of", num1, "and", num2, "inside the \'find_mix\' function =", num2)
    else:
        print("Bigger of", num1, "and", num2, "inside the \'find_max\' function =", num1)

def main():
    print("I am inside the main function.\n")
    find_sum()
    find_min()
    find_max()
    print("\nLeaving the main function.")

main()