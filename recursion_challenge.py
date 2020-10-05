'''Creating a function to check if input is a palindrome'''
def palindrome_check(x):
    x = list(str(x))
    if x[0:] == list(reversed(x[0:])):
         return True
    else:
        return False


print("\n*******************")
print("PALINDROME CHECKER")
print("*******************\n")

'''Asking for user to input something to check 
and running it through the palindrome check function'''
n=input("Enter a word or number to check: ")
ans=palindrome_check(n)

'''analyzing output of function and returning a message'''
if ans==True:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")