num=int(input("Enter a number, I will square up to this number using for loop: "))
n=1
num2=num
print("Number\tSquare")
for num2 in range(n,num2+1):
    sq=num2*num2
    print (num2, "\t", sq)

print("\n\nNow printing in Backward direction")
print("Number\tSquare")
for num in range(num,0,-1):
    sq=num*num
    print (num, "\t", sq)