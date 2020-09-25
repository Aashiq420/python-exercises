avg = float(input("What was your average speed in km/h?: "))
allow = float(input("What was the allowed speed on the road?: "))

if avg>allow:
    delta = avg-allow
    points = delta//5
    print("Points: "+str(points))
elif avg<=allow and avg>=0:
    print("You were within the speed limit")
else:
    print("Come on. Use positive numbers")