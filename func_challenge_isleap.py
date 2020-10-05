def distance_from_zero(input1):
    try:
        input1 = float(input1)
        if input1<0:
            ans = input1*-1
        else:
            ans = input1
    except ValueError:
        ans = "Nope"
    return ans
x = input("ENTER THE THING: ")
print(distance_from_zero(x))

def is_leap(year):
    if year%4==0:
        if year%400==0:
            return True
        elif year%100==0:
            return False
        

yr = int(input("Enter a year: "))
print(is_leap(yr))