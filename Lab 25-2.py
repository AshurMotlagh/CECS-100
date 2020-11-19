num = 10


def main():
    global num
    print("Global variable inside main=", num)
    num = 15
    print("Now changed gloabl variable inside main=", num)
    half(num)


def half(x):
    half = x/2
    print("Half of global variable is =", half)


main()
