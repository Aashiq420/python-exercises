from playsound import playsound
from tkinter import *

def play():
    playsound(name.get()+'.mp3')

#tkinter window stuff
root = Tk()
root.geometry('400x400')
root.title('Music Player')

#creating buttons entry fields and labels
#entry
name = Entry(root)
name.place(x=175,y=10)

#label
name_label = Label(root, text='Enter song to play:')
name_label.place(x=10,y=10)

#buttons
play_btn = Button(root, text='Play',command=play)
play_btn.place(x=60,y=60)
quit_btn = Button(root, text='Quit',command=root.destroy)
quit_btn.place(x=275,y=60)

#looping window
root.mainloop()

