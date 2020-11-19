def personal_info():
    print("My name is Ashur Motlagh")
    print("In live in California.")
    print("My phone number is: 714-726-4503")

def work_info():
    name=str(input("Enter your name: "))
    age=int(input("Enter your age: "))
    salary=int(input("Enter your salary: "))
    bonus=int(input("Enter your bonus: "))

    pay=float(salary+bonus)

    print("\nHere is your information!")
    print("Your name: ", name)
    print("Your Age: ", age)
    print("Your total pay: ", pay)

def main():
    print("I am inside the main function. \n")
    print("Calling \"personal_info\" function.")
    print("Here \"programmer\" is giving his information.\n")
    personal_info()

    print("\nCalling \"work_info\" function.")
    print("Here \"user\" is giving his information.\n")
    work_info()
    print("\nDone writing personal information and work information inside main")

main()