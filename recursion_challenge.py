def palindrome_check(x):
    x = list(str(x))
    if x[0:] == list(reversed(x[0:])):
         return True
    else:
        return False


print("*******************")
print("PALINDROME CHECKER")
print("*******************\n")

n=input("Enter a word or number to check: ")
ans=palindrome_check(n)

if ans==True:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")