while True:
    try:
        avg = float(input("What was your average speed in km/h?: "))
        allow = float(input("What was the allowed speed on the road?: "))
        break
    except ValueError:
        print("Please enter a numerical value!\n")

if avg>allow:
    delta = avg-allow
    points = delta//5
    print("Points: "+str(points))
    if points>12:
        print("Time to go to jail!")
elif avg<=allow and avg>=0:
    print("You were within the speed limit")
else:
    print("Come on. Use positive numbers.")  