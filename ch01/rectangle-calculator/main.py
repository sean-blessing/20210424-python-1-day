print("Welcome to the area and perimeter calculator!")

choice = "y"

while choice == "y":
    length = int(input("enter length:\t"))
    width = int(input("enter width:\t"))

    perimeter = 2*length + 2*width
    area = length * width
    print(f"Area:\t\t{area}")
    print(f"Perimeter\t{perimeter}")

    choice = input("Try again?")

print("Bye")
