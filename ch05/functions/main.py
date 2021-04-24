def print_something():
    print("something")


def sum(nbr_1, nbr_2=0):
    return (nbr_1 + nbr_2)


print_something()
print(sum(5, 9))
print(sum(2))


# variable arguments (*args)
def add(*nbrs):
    sum = 0
    for nbr in nbrs:
        sum += nbr
    return sum


print(add(1, 2, 3))
print(add(1, 2, 3, 5, 6, 7, 8, 9, 2, 3, 34, 5, 6, 6, 7, 78, 99))
# print(add(range(1, 10)))

#key word arguments (**kwargs)
def print_stuff(name, age, gender):
    print(f"{name}, {age}, {gender}")

print_stuff(age=27, gender="female", name="Sally")
print_stuff(age=30, gender= "male", name="Steve")
