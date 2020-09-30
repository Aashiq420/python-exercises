list1=[]
try:
    x = int(input("Enter a number: "))
    list1.append(x)
except ValueError:
    print("Invalid entry")
while True:
    try:
        y = int(input("Enter another number: (or type anything else to stop)\n"))
        if isinstance(y, int)==True:
            list1.append(int(y))
    except ValueError:
       break
print("\nThese are the numbers you entered:")
print(list1)

high = 0
for i in range(len(list1)):
    if list1[i]>high:
        high = list1[i]
list1=list(dict.fromkeys(list1))   
print("The highest number in the list is:",high)
print("This is the list without duplicates:")
print(list1)