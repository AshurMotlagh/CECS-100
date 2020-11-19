month = int(input("Enter the month you were born (00-12): "))
day = int(input("Enter the day you were born: "))
year = int(input("Enter the last 2 numbers of the year you were born: "))

month = month*4
month = month+13
month = month*25
month = month-200
month = month+day
month = month*2
month = month-40
month = month*50
month = month+year
month = month-10500

print (month, "is your birthday")
