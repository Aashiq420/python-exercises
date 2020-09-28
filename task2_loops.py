for i in range(1,6):
    x="*"
    print(x*i)
    i=i+1
    if i==6:
        for j in reversed(range(1,5)):
            y="*"
            print(y*j)
            j=j+1