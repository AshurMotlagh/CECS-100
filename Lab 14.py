print("------------------------------------Exercise A -----------------------------------------------")
print("Display all numbers 1-5, using list of numbers.")
for num in (1,2,3,4,5):
    print (num, end=' ')

print ("\n")

print("------------------------------------Exercise B --------------------------------------------------")
print("Print Hello World five times using range function with for loop.")
for num in range(5):
    print ("Hello World")
print("\n")

print("------------------------------------Exercise C --------------------------------------------------")
print("Display all numbers 1-10, using range function with for loop.")
for a in range(11):
    print (a, end=' ')
print ("\n")

print("------------------------------------Exercise D --------------------------------------------------")
print("Print all the even numbers between 1-10, using range function with for loop.")
for b in range(2,11,2):
    print (b, end=' ')
print("\n")

print("------------------------------------Exercise E --------------------------------------------------")
print("Print all the odd numbers between 1-10, using range function with for loop.")
for c in range(1,10,2):
    print (c, end=' ')
print("\n")

print("------------------------------------Exercise F --------------------------------------------------")
num = int(input("Enter a number, I will print all the numbers from one to this number: "))
i = num
print("Numbers in forward direction.")
for num in range(1,num+1):
    print(num, end=' ')
print("\n")
print("\nNumbers in backward direction.")
for i in range(i,0,-1):
    print(i, end=' ')