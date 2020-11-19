start=3.5
steps=3
sn=10
num=start
sum=0
sum2=sum

print("-----------using \'while loop\'-----------\n")
print("First 10 numbers starting at 3.5")
while sn>=1:
    print(start,end=' ')
    sum+=start
    sn=sn-1
    start=start+steps
print("\nTheir sum =", sum)


print("\n----------using \'for loop\'----------\n")
print("First 10 numbers starting at 3.5")
for n in range(10):
    print(num, end=' ')
    sum2+=num
    num=num+steps
print("\nTheir sum =", sum2)
