'''
petrol = 45
while petrol>0:
    print("Vroom")
    petrol-=1
    if petrol == 10:
        print("Fill up!")
        continue


ages=[18, 21, 16, 12]
for age in ages:
    if age>=18:
        print("Come on in")
    elif age>=16:
        print("Not quite yet")
    else:
        print("Get outta here!")

adj =["red", "big", "tasty"]
fruit =["apple", "bannana", "cherry"]

for x in adj:
    for y in fruit:
        print(x, y)

for x in range(6):
    print(x)
for x in [0, 1, 2]:
    pass


x=0
while x<100:
    x=x+1
    if x%15 == 0:
        print("FizzBuzz")
    elif x%5 == 0:
        print("Buzz")
    elif x%3 == 0:
        print("Fizz")
    else:
        print(x)
'''
y=0
for y in range(100):
    y=y+1
    if y%15 == 0:
        print("FizzBuzz")
    elif y%5 == 0:
        print("Buzz")
    elif y%3 == 0:
        print("Fizz")
    else:
        print(y)
