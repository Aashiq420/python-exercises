x = input("Type some words: \n")
print("First Letter: "+x[0])
print("Last letter: "+x[-1])

y = input("Would you like to convert these words to piglatin? (y/n): ")
#piglatin 
if y == 'y':
    x = x.split()
    for i in range(len(x)):
        if x[i][0] in "aeiou":
             x[i] += 'yay'
        else:
             x[i]=x[i][1:]+x[i][0]
             x[i]+='ay'
    x = ' '.join(x)
    print(x)
elif y == 'n':
    print("Understandable, have a nice day!")
else:
    print("You have to enter either 'y' or 'n'. Program will now end")