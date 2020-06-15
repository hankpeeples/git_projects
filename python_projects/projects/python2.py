# ----- Lists -----
print("\n-----Listing-----")
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
print("\n-List Print Loop-")
for x in mylist:
    print(x)

print("\n-Full Version-")
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers) # prints [1, 2, 3]
print(strings) # prints ['hello', 'world']
print("The second name on the names list is %s\n" % second_name)

# math ops.
print("\n-----(Power) math operator-----")
print(7 ** 2) # (**) works as power operator (7^2)

# operators with lists
print("\n-----Operators with lists-----")
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# wild list
print("\n-----Some big list-----")
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")