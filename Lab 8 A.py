'''
Ashur Motlagh
018319910
Lab 8 A
'''
print ("Enter your name:", end='')
name=input ()
#another way to do this would be, name = input ("Enter your name")

print ("Enter your age:", end='')
age= int(input())
#name= input ("enter your name")

salary=int(input("Enter Salary:"))
bonus= int(input("Enter Bonus:"))
totalpay= float(salary+bonus)
print ("\nHere is your information!")
print ("Your name: ",name)
print("Your Age: ",age)
print("Your total pay: ", totalpay)

