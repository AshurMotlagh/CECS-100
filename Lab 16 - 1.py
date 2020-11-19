start = int(input("Enter your start number: "))
end = int(input("Enter your end number: "))
increment = int(input("Enter increment number: "))

while (increment <= 0):
    print("\nIncrement number must be greater than 0.")
    increment = int(input("Enter increment number again: "))

while (end <= start):
    print("\nEnd number must be greater than start number.")
    end = int(input("Enter the end number again: "))

print("\nHere is the list of numbers.")
for start in range(start, end+1, increment):
    print (start, end=' ')