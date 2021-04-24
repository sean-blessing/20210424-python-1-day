print("Hello World!")

# this is a comment
# there are no multi line comments
# cntl / will add a comment on the selected lines

# statements don't end in ;
a = 5
# \ is a line break, continues stmt
result = 4 + 6 + 7 \
         + 8 + 9
print(result)

# determine the type of a var
print(type(result))

# arithmetic operators
print(10/2)
print(10%3)
print(5*5)

# print always gives a new line at end
print("hello")
print("there")

# end attribute
print("hello", end=" ")
print("class")

# seperator
print("a", "b", "c", "d", sep="-")

# formatted print
days_in_week = 7
# this doesn't work
#print("There are "+days_in_week+" days in a week.")
print("There are "+str(days_in_week)+" days in a week.")
float_1 = 35.7
print(f"There are {days_in_week} days in a week.  float_1 is {float_1}")

# get user input
name = input("What's your name? ")
print(f"Hello, {name}!")
birth_month = input("What month were you born (numeric)? ")
print(birth_month)
print(type(birth_month))
birth_month = int(birth_month)
print(type(birth_month))

nbr_1 = int(input("Enter a whole #: "))
print(nbr_1)

import sys
# sys.argv usage
print(sys.argv[0])

code = "r"

if code=="r":
    print("color is red")
elif code == "b":
    print("blue")
else:
    print("wrong pic")

choice = "y"

while choice == "y":
    print("hello")
    choice = input("Try again? ")
print("bye")