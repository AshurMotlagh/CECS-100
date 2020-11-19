
'''
Ashur Motlagh
lab 12
-------------------------Exercise C----------------------------------
'''
sleepy = True
hungry = True
if (sleepy and hungry):
    print ("Very Bad :(")
else:
    print ("Life is Good :)")
if (sleepy or hungry) :
    print ("not too bad, OK")
else:
    print("Take care :)")
    

print ("\n")
print ("\n")

#----------------------Exercise A------------------------------------
'''
THIS IS THE FIRST WAY
num = int(input("Pick a number 0 through 200: "))
if num>=0 and num<=200 :        # or 0<=num<=200:
    print ("\"the number is valid\"")
else:
    print ("\"the number is not valid\"")
'''
num = int(input("Pick a number 0 through 200: "))
if num>=0 and num<=200 :
    num=True
else:
    num=False
    
if num:
    print ("\"the number is valid\"")
else:
    print ("\"the number is not valid\"")



print ("\n")
print ("\n")

#---------------------Exercise B--------------------------------------
print ("Enter three different numbers, I will find the \"Smallest Number\"")
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))
if n1<n3 and n1 < n2:
    print (" The smallest number is ", n1)
elif n2<n1 and n2<n2:
    print (" The smallest number is ", n2)
else:
    print (" The smallest number is ", n3)