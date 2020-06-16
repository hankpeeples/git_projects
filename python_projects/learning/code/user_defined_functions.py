#import line here (duh)


print("\nFirst 2 sections are only in programming_basics notes file")

#---defining function
print("\n--- 3. Defining Function")
def my_function():
    print("This is my_function!")
    print("A second string\n")

my_function()

#---adding arguments to function
print("---- 4. Adding Arguments to a Function")
def my_function2(str1, str2):
    print(f'{str1}')
    print(f'{str2}\n')

my_function2("Argument 1", "Argument 2")

#default Arguments
print("----- 5. Default Argument")
def print_something(name = 'name', age = 'unknown'):
    print("My name is", name, "and my age is", age)

print_something() #default
print_something('Hank', 20) #given values

#keyword argument 
print("\n------ 6. Keyword Argument")
def print_something2(name = 'name', age = 'unknown'):
    print("My name is", name, "and my age is", age)

print_something2(age = 20, name = 'Hank')

#infinite arguments
print("\n------- 7. Infinite Arguments")
def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Nick", "Hank", "Jack", "Perry")

#return values from functions
print("\n-------- 8. Return values from functions")
def do_math(num1, num2):
    return num1 + num2
    
math1 = do_math(5, 7)
math2 = do_math(4, 36)

print(f'First sum is {math1} and second sum is {math2}')

#if, elif, else statements
print("\n--------- 9. If, elif, else statements")
check = True

if check == False:
    print("It is False")
elif check == "Yo":
    print("Wassup")
elif check == "Hamburger":
    print("Burger time bitch")
else:
    print("It is True")

#for/while loops
print("\n---------- 10. For/While Loops")
print("- For Loop")
numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

print("-- While Loop")
run = True
current = 1

while run:
    if current == 20:
        run = False

    else:
        print(current)
        current += 1

#import libraries
print("\n----------- 11. Importing Libraries")
import re #regex

string = "'I AM NOT YELLING', she said. Though we knew it was not true."
print(string)

new = re.sub('[A-Z]', '', string) 
print(new)
new = re.sub('[a-z]', '', string)
print(new)
new = re.sub('[.,\']', '', string)
print(new)
new = re.sub('[.,\'a-zB-Z]', '', string)
print(new)
new = re.sub('[.,\'A-Z+" "]', '', string) # +" " removes spaces
print(new)

string = string + "6 298 - 345"
print(string)
new = re.sub('[^0-9]', '', string) # ^0-9 removes everything except numbers
print(new)
