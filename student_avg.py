from datetime import *

std_name = input("Enter first name: ")
std_lastname = input("Enter last name: ")
mark_1 = float(input("Enter mark for test 1: "))
mark_2 = float(input("Enter mark for test 2: "))
mark_3 = float(input("Enter mark for test 3: "))

def average(x,y,z):
    avg = (x+y+z)/3
    return round(avg,2)

def passfail(x):
    if x<50:
        return "Fail"
    elif x>=50:
        return "Pass"

result = average(mark_1,mark_2,mark_3)
print("*********************************************")
print("Report Card for",std_name,std_lastname)
print("*********************************************")
print("The average mark of the 3 tests is:",result)
print("Result:",passfail(result))