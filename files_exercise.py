from tkinter import *

root = Tk()
root.title("Text Files")
root.geometry('600x500')
root.configure(bg='red')
class weekend:
    def __init__(self):
        #label and textbox
        heading = Label(root, text="My weekend activities", font=('Helvetica', 20), bg='red')
        self.display_text = Text(root, height=7, width=60,bg='red')
        box = Text(root, height=7, width=60)

        #buttons
        create_btn = Button(root, text="Create textfile")
        display_btn = Button(root, text="Display")
        append_btn = Button(root, text="Append data")
        clear_btn = Button(root, text="Clear", command=self.clear)
        exit_btn = Button(root, text="Exit")

        #text placements
        heading.place(x=50, y=50)
        self.display_text.place(x=50, y=280)
        box.place(x=50, y=90)

        #btn placements
        create_btn.place(x=45,y=235)
        display_btn.place(x=175,y=235)
        append_btn.place(x=260,y=235)
        clear_btn.place(x=380,y=235)
        exit_btn.place(x=450,y=235)


        
    def create():
        pass

    def display():
        pass

    def append():
        pass

    def clear(self):
        self.display_text.delete('1.0', END)
        

run = weekend()
root.mainloop()