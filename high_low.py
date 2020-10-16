import random
from tkinter import *

num = random.randrange(1, 100)
print(num)

window = Tk()
window.geometry("350x150")
window.title("Number Guessing Game")


statement_label =Label(text="I have chosen a number between 1 and 100").grid(row=0, column=0,padx=10,pady=10)
user_guess = Entry(window)
ans_label = Label(text="Take a guess")

def game():   
    if num == int(user_guess.get()):
        ans_label.config(text="Congratulations! "+str(num)+" was the correct number")
    elif num < int(user_guess.get()):
        ans_label.config(text="Too high. Try again")     
    elif num > int(user_guess.get()):
        ans_label.config(text="Too low. Try again")

guessbtn = Button(window, text="Try", command=game).grid(row=3, column=0)
user_guess.grid(row=2, column=0)
ans_label.grid(row=1,column=0)
window.mainloop()
