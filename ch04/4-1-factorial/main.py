print("Welcome to the factorial calculator")

choice = "y"

while choice=="y":
    nbr = int(input("Enter a # > 0 and < 10: "))
    fact = 1
    for n in range(1, nbr+1):
        fact *= n
    print(f"The factorial is {fact}.")

    choice = input("Again?")

print("bye")