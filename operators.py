'''Task 1 - Pythagorus'''
import math

a = input("Do you need to calculate the hypotenuse? (y/n): ")
print("\n")

while a != "y" and a != "n":
    print("Please enter either 'y' for yes or 'n' for no")
    print("\n")
    a = input("Do you need to calculate the hypotenuse? (y/n): ")
    print("\n")

if a == 'y':
    b = float(input("Enter the length of side 1: "))
    print("\n")
    c = float(input("Enter the length of side 2: "))
    print("\n")
    h = math.sqrt(b*b+c*c)
    print("The length of the hypotenuse is: "+str(h))
elif a == 'n':
    h = float(input("Enter the length of the hypotenuse: "))
    print("\n")
    b = float(input("Enter the length of the other known side: "))
    print("\n")
    c = math.sqrt(h*h-b*b)
    print("The length of the third side is: "+str(c))

