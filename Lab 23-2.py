def main():
    name1 = str(input("Enter your first friends name: "))
    name2 = str(input("Enter your seconds friends name: "))
    name3 = str(input("Enter your third friends name: "))
    file = open('newfile.txt', 'w')
    file.write(name1)
    file.write("\n")
    file.write(name2)
    file.write("\n")
    file.write(name3)
    file.close()
    print("Done writing. Now i am reading their name from the same file.")

    afile = open('newfile.txt', 'r')
    file_content = afile.read()
    afile.close()

    print(file_content)


main()
