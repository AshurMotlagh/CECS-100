print("Running on a particular treadmill you will burn 4.2 calories per minute")
ans = "yes"
while 'y' or 'Y' in ans:  # while ans == "yes" or ans == "YES" or ans == "Yes" or ans == "Y" or ans == "y":
    user = int(input('\nHow many minutes did you walk?'))
    result = user * 4.2
    print("Calories burned after", user, "minutes =", result, "calories")
    ans = str(input("\nDo you want to calculate more? "))

print("\nThanks for using this program!")
