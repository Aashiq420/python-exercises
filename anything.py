#mark grader


def grader(mark):
    if mark >=80 and mark<100:
        print("Grade: A","with a mark of:",mark)
    elif mark >=70 and mark<79:
        print("Grade: B")
    elif mark >=60 and mark<69:
        print("Grade: C")
    elif mark>=50 and mark<59:
        print("Grade: D")
    elif mark>=0 and mark<50:
        print("Fail")
    elif mark>100 or mark<0:
        print("invalid entry")


user_input = float(input("Enter your mark as percentage: "))
grader(user_input)



