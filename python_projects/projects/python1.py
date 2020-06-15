print("\n")

a = "thm{knasbab6sgausb6u}"

if "thm" in a:
    print(a)
else:
    print("nope")

print("\n-----Input Practice-----")
name = str(input("Enter name: "))
type(name)
print("Hello,", name)
    
b = int(input("Input a number: "))
type(b)
print(b)

# Function practice
print("\n-----Function Practice?-----")
def userName():
    name = input("Please enter your name: ")
    return name

print(userName())

def tryhackme(creator, assignment):
    print(creator, assignment)
    return

name = input("Input creator name: ")
assignment = input("Input assignment: ")
tryhackme(name, assignment)

# Auto Increase using while loop
print("\n-----Auto Increase using While-----")
i = 1
while i <= 5:
    print(i)
    i += 1

# Printing from array using for loop
print("\n-----Printing from Array using for loop-----")
admins = ["Skidy", "Ashu", "Dork"]

for i in admins:
    print(i)

for i in range(0, 20, 2):
    print(i)
else:
    print("Done")

# ---- Interacting with files ---- #
#text = open("file_name", "mode")
print("\n-----Some Shit with a file-----")
file = open("ptest.txt", "r")
print(file.read()) #file.readlines() / file.readline()

file = open("ptest.txt", "r")
for line in file:
    print(line, end='')
    
file = open("ptest.txt", "w")
file.write("Writing to file from python script") #overrides file content

print("\n")