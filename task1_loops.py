import random

ans = random.randint(1, 10)
print(ans)
guesses_left = 3

print("*****************************")
print("WELCOME TO THE GUESSING GAME")
print("*****************************\n")

while guesses_left>0:
    if guesses_left == 3:
        guess = int(input("I have chosen a number between 1 and 10. What is your guess? "))
        guesses_left = guesses_left - 1
        continue
    if guesses_left<3 and guess != ans:
        print("Incorrect. You have ",guesses_left," attempt(s) remaining")
        guess = int(input("Try another guess: "))
        guesses_left = guesses_left - 1
        continue
    if guess == ans:
        print("Congratulations! You have guessed correctly!")
        break
if guesses_left == 0:
    print("Unfortunately you have used all 3 of your attempts. Game Over!")
    


    
