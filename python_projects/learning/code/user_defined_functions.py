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
