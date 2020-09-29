def even_odd(x):
    if x%2==0:
        return True
        
num = int(input("Enter a number: "))
ans = even_odd(num)
if ans == True:
    print(num, "is an even number")
else:
    print(num, "is an odd number")