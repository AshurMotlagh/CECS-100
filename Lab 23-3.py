def main():
    num = int(input("Enter a number, I will square up to this number using for loop: "))
    forward(num)
    backward(num)


def forward(new):
    print("Number\tSquare")
    n=1
    for num2 in range(n, new + 1):
        sq = num2 * num2
        print(num2, "\t", sq)


def backward(new):
    print("Number\tSquare")
    for new in range(new, 0, -1):
        sq = new * new
        print(new, "\t", sq)


main()
