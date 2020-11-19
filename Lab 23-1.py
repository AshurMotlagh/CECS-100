def main():
    print("I am writing my friends name to the file.")
    file = open('ashurfile.txt', 'w')
    file.write("Aaron \nFares \nArian")
    file.close()
    print('Done writing. Now i am reading their name from the same file.')

    afile = open('ashurfile.txt', 'r')
    file_content = afile.read()
    afile.close()

    print(file_content)


main()
