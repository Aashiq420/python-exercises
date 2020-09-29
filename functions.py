'''
def greet(name):
    print("Hello ", name)
    print("What you then say bru?")

greet(input("Enter your name: "))
print("This is outside greet()")

def calc_sum(n):
    if n==1:
        return 1
    else:
        return n+calc_sum(n-1)

sum = calc_sum(5)
print(sum)'''

def add(x,y):
    ans = x+y
    return ans

n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
soln = add(n1,n2)
print(n1," + ",n2 ," = ", round(soln,3))
