'''n1 = float(input("Enter a number: "))
n2 = float(input("Enter another number: "))

if n1>n2:
    print(str(n1)+" is greater.")
elif n2>n1:
    print(str(n2)+" is greater.")
else:
    print("The numbers are equal")'''

'''*************************************************************'''

'''x=10
if x<=15:
    if x==10:
        print("play cricket")
    else:
        print("play kabadi")    
else:
    print("dont play a game")'''

'''***************************************************************'''

while True:
    try:
        mark = float(input("Enter student mark as percentage: "))
        break
    except ValueError:
        print("Please enter a numerical value!\n")


while mark<=100 and mark>=0:
    if mark>=80 and mark<=100:
        print("Grade A")
        break
    elif mark>=70 and mark<=79:
        print("Grade B")
        break
    elif mark>=50 and mark<=69:
        print("Grade C")
        break
    elif mark>=40 and mark<=49:
        print("Grade D")
        break
    else:
        print("Grade F")
        break
else:
    print("It is not possible to have more than 100%, or less than 0%")
    