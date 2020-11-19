pi=3.14
def main():
    rad=float(input("Enter the radius of the circle: "))
    area=find_area(rad)
    print("Value of PI inside main is: ", pi)
    print("Area of the circle = ", area)
    print("Area of the circle upto 2 decimal points = ", format(area, '.2f'))

def find_area(a):
    area=pi*(a**2)
    return area

main()