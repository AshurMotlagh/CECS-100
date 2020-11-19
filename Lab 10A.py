x= int(input("Enter your First Score: "))
y= int(input("Enter your Second Score: "))
z= int(input("Enter your Third Score: "))
avg=(x+y+z)/3
print("The average score is: ", format(avg,'.2f'))
if avg >=95:
    print("Congratulations!!")
    print("That is a great average")
