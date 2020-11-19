print("I am writing my friend's name to the file.")
am = int(input('How many friends name do you want to input: '))
myfile = open('friend.txt', 'w')
for i in range(am):
    print('Enter the name of your friend # ', i+1, end=" ")
    name = input()
    myfile.write(name+ '\n')

myfile.close()

print("\n****Done writing to the file****")
print("\n******Now printing only my first 2 friends name.******\n")

myfile = open('friend.txt', 'r')
fri = myfile.readline()
fri = fri.rstrip()
fri2 = myfile.readline()
fri2 = fri2.rstrip()

print(fri)
print(fri2)
