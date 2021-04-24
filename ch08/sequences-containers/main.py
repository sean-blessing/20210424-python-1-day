name = "Robert Nesta Marley"
print('name:', name)
print('length of name', len(name))
#get portions of the name by index and slicing
print('first char:', name[0])
#get first name
# where's the first space?
idx_1 = name.index(" ")
f_name = name[0:idx_1]
print(f_name)
idx_2 = name.index(" ", idx_1+1)
m_name = name[idx_1+1: idx_2]
print(m_name)
l_name = name[idx_2+1:len(name)]
print(l_name)
for str in name:
    print(str, end=" ")
print()

# a list is noted by square brackets
letters = ["a", "b", "c", "d", "e", "f"]
print('first letter', letters[0])
print('last letter', letters[5])
#print('outside list', letters[6]) -> produces IndexError
print('using len', letters[len(letters)-1])
print('last letter', letters[-1])
print('2nd thru 4th letters', letters[1:4])
# replacing an element
letters[4] = "z"
print(letters)
# append
letters.append("z")
print(letters)
# remove using pop and pop??
print('pop', letters.pop())
print(letters)

#count
letters.append("c")
print(letters)
print('count c:', letters.count("c"))

#range
print('range 1 to 10:', range(1, 10))
print('range 1 to 10 - list:', list(range(1, 10)))

#for...in
for letter in letters:
    print(letter, end=" ")
print()

#for using index
for i in range(0, len(letters)):
    print(f"letter {i}: {letters[i]}")

# does our letters list contain 'z'?
if "z" in letters:
    print("yep, z is in there!")

# use * on a string
str_1 = "a" * 10
print('str_1:', str_1)

letters = letters * 2
print('letters*2:', letters)

# a tuple
tuple_1 = (1, 2, 3, 4, 5)
print(tuple_1)
#tuple_1[2] = 7 -> can't modify a tuple

# random choice
import random
print('random choice from tuple:', random.choice(tuple_1))
print('random choice from tuple:', random.choice(tuple_1))
print('random choice from tuple:', random.choice(tuple_1))

# dictionaries (key:value) pairs
spanish_english = {
    "uno": "one",
    "dos": "two",
    "tres": "three",
    1: "one"
}
print(spanish_english)
#get value by key
print(spanish_english["dos"])
print(spanish_english.get("dos"))
# add an element
spanish_english["quatro"] = "four"
print(spanish_english)
# change an element
spanish_english[1] = 11111
print(spanish_english)

# iterating over the dict
# keys
for k in spanish_english:
    print(k)
# values
for v in spanish_english.values():
    print(v)
# key:value pairs
for k, v in spanish_english.items():
    print(f"key {k}: value {v}")
# does a key exist?
if "uno" in spanish_english:
    print("uno is in there!")
elif "dos" in spanish_english:
    print("dos is in there!")
else:
    print("doesn't exist")

# pop(key), popitem - removes last
print('popitem', spanish_english.popitem())
print('pop(1)', spanish_english.pop(1))
print(spanish_english)



