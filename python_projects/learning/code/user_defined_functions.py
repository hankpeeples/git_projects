

#---defining function
#def = define function
def my_function():
    print("\nThis is my_function!")
    print("A second string\n")

my_function()

#---adding arguments to function
def my_function2(str1, str2):
    print(f'\t{str1}')
    print(f'\t{str2}\n')

my_function2("Argument 1", "Argument 2")


#default Arguments
def print_something(name = 'name', age = 'unknown'):
    print("My name is", name, "and my age is", age)

print_something() #default
print_something('Hank', 20) #given values
