print("Welcome")

nbr_1 = 0;
valid_nbr = False
while not valid_nbr:
    try:
        nbr_1 = int(input("Enter a whole number: "))
        valid_nbr = True
    except ValueError:
        print("Invalid whole #.  Try again.")
    finally:
        print("finally")

print(nbr_1)
print(type(nbr_1))

print("Bye")