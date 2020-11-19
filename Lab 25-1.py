# This lab is teaching us to use file append mode
ans = "yes"
while ans[0].lower() == "y":
    print("I am writing 3 numbers to the file.")
    f1 = int(input("Enter first number: "))
    f2 = int(input("Enter second number: "))
    f3 = int(input("Enter third number: "))

    myfile = open('lab25.txt', 'a')
    myfile.write(str(f1) + "\n")
    myfile.write(str(f2) + "\n")
    myfile.write(str(f3) + "\n")
    myfile.close()
    print("Done writing to the file")

    total = 0
    print("\nNow reading these numbers from the file")
    infile = open('lab25.txt', 'r')
    line = infile.readline()
    while(line != ''):
        total = total + 1
        line = infile.readline()
    print("Total number of numbers inside the file is: ", total)
    infile.close()

    ans = str(input("\nDo you want to try out again? "))

print('Thanks for using this program')
