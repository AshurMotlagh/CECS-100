seconds = int(input("Enter the number of seconds: "))

hour=seconds//3600
minutes= (seconds//60) %60
seconds= seconds % 60

print("Here is the time in hours, minutes, and seconds:")
print ("Hours =", float(hour))
print ("Minutes =", float(minutes))
print ("Seconds =", float(seconds))
