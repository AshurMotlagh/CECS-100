#----------Exercise B-------

x= input("Enter a name (last name first):")
y= input("Enter another name (last name first):")
print("Here are the names, listed alphabetically.")
if x<y:
    print (x)
    print (y)
else:
    print (y)
    print (x)

print ("\n")
print ("\n")

#----------Exercise A------

fl= int(input("Enter length of the first rectangle:"))
fw= int(input("Enter width of the first rectangle:"))
print ("\n")
sl= int(input("Enter length of the second rectangle:"))
sw= int(input("Enter width of the second rectangle:"))
a1= fl*fw
a2= sl*sw
print ("\n")
if a1>a2:
    print ("Area of the first rectangle is bigger!")
elif a1<a2:
    print ("Area of the second rectangle is bigger!")
else:
    print ("Both Rectangles have the same area!")


print ("\n")
print ("\n")

#------------Exercise C---------
num= int(input("Enter number 1-7 and this will correspond with the day of the week: "))
if num==1:
    print ("Monday")
elif num==2:
    print ("Tuesday")
elif num==3:
    print ("Wednesday")
elif num==4:
    print ("Thursday")
elif num==5:
    print ("Friday")
elif num==6:
    print ("Saturday")
elif num==7:
    print ("Sunday")
else:
    print ("Please enter a number from 1-7!")
