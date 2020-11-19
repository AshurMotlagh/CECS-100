def main():
    num = int(input("Enter a number, I will print all the numbers from one to this number: "))
    all_num(num)
    all_odd(num)
    all_even(num)


def all_num(x):
    print("\nALL the numbers.")
    for a in range(x):
        print(a, end=' ')


def all_even(x):
    print('\nALL ODD numbers.')
    for b in range(2, x, 2):
        print(b, end=' ')


def all_odd(x):
    print("\nALL EVEN numbers.")
    for c in range(1, x, 2):
        print(c, end=' ')


main()
