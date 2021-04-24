print("Welcome to the Temperature Converter")

choice = "y"

while choice == "y":
    f = float(input("Enter degrees in F: "))
    c = (f-32) * (5/9)
    c = round(c, 2)
    print(f"Degrees in Celcius: {c}")

    choice = input("try again?")

print("bye")
    