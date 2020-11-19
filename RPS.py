import sys


def main():
    print("In this program you will be playing \"Rock Paper and Scissors\" with a 33.33% chance of winning")
    while True:
        print("User input is wrong")
        answer = str(input("Rock! Paper! Scissors!: ")).lower()  # here we are asking user for their response
        while answer != 'rock' or answer != "paper" or answer != 'scissors':
            break
        while answer == 'rock' or answer == "paper" or answer == 'scissors':
            choice = rps()
            print("System chose:", choice, "You chose:", answer)
            if choice == 'paper':
                if answer == choice:
                    print("Tie")
                elif answer == 'rock':
                    print("You lose. Paper beats Rock.")
                elif answer == 'scissors':
                    print("You win. Scissors beats Paper")

            elif choice == 'rock':
                if answer == choice:
                    print("Tie")
                elif answer == 'paper':
                    print("You win. Paper beats Rock")
                elif answer == 'scissors':
                    print("You lose. Rock beats Scissors")

            elif choice == 'scissors':
                if answer == choice:
                    print("Tie")
                elif answer == 'paper':
                    print("You lose. Scissors beats Paper")
                elif answer == 'rock':
                    print("You win. Rock beats Scissors")

            flag = input("Do you want to continue? (Y/N)").upper()
            if flag[0] == 'Y':
                answer = str(input("Rock! Paper! Scissors!: ")).lower()  # here we are asking user for their response
            else:
                sys.exit()


def rps():  # here we are doing the probability of winning
    num = number()
    if num <= 25:
        choice = 'paper'

    elif 26 <= num <= 50:
        choice = 'rock'

    else:
        choice = 'scissors'
    return choice


def number():  # this is the function for getting the random number for the function rps
    import random
    for x in range(1):
        rand_num = (random.randint(1, 76))
        return rand_num


main()
