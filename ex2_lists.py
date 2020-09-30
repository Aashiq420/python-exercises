def check(x,y):
    for i in x:
        for j in y:
            if x[i]==y[j]:
                return True

ages=[2,12,12,14,15,16,16, 17,18, 14, 20, 20]
ages1=[2,4,12,14,15,16,16, 17,18, 14, 20, 20]
print(check(ages,ages1))