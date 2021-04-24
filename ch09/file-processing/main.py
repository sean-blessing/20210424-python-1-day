# read in the file and print
# read() method returns contents as one string
with open("hobbies.txt") as hobbies_file:
    contents = hobbies_file.read()
print(contents)

print("print a line...")
# readline() method returns one line as string
with open("hobbies.txt") as hobbies_file:
    line = hobbies_file.readline()
print(line)

print("print all lines...")
# readlines() method returns a list of all lines
with open("hobbies.txt") as hobbies_file:
    lines = hobbies_file.readlines()
print(lines)
# couldn't figure out how to remove \n

# create a file from list
family = ["Sean", "Amy", "Bailey", "Breck"]
handle = open("family.txt", "w")
for member in family:
    handle.write(member+"\n")
handle.close()
print("family file written")
