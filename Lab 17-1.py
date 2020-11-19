row = 0
while row<=1:
    row = int(input("Enter a positive row number: "))

print('\n')

column = 0
while column <= 1:
    column = int(input("Enter a positive column number: "))

print("\n******Here is the Rectangle*****")
for r in range(row):
    for c in range(column):
        print("*", end=" ")
    print()
