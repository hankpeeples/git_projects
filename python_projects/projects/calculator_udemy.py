import re

print("Our Magical Calculator")

previous = 0
run = True

def perform_math():
    equation = input("Enter equation: ")
    print("You typed,", equation)

while run:
    perform_math()