print("I am writing 3 numbers to the file.")
f1 = int(input("Enter first number: "))
f2 = int(input("Enter second number: "))
f3 = int(input("Enter third number: "))

myfile = open('friend.txt', 'w')
myfile.write(str(f1)+"\n")
myfile.write(str(f2)+"\n")
myfile.write(str(f3)+"\n")
myfile.close()

print("\nDone writing to the file")
print("Now reading these numbers from the file")
myfile = open('friend.txt', 'r')
n1 = int(myfile.readline())
n2 = int(myfile.readline())
n3 = int(myfile.readline())
myfile.close()

print("number one = ", n1)
print("number two = ", n2)
print("number three = ", n3)

sum = f1+f2+f3
print("\nSum of these numbers = ", sum)