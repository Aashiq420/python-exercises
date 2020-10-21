from tkinter import *

root=Tk()
root.title("Aashiq's Program")
root.geometry("800x800")

class sick:                     #Parent class of influenza and cancer classes
    def __init__(self, master):
        myFrame=Frame(master)
        myFrame.pack()

        sickness_code = Label(master, text="Sickness Code:").place(x=5,y=25,anchor="w")
        treatment_duration = Label(master, text="Duration of Treatment:").place(x=5,y=50,anchor="w")
        doc_prac_num = Label(master, text="Doctor's Practice Number:").place(x=5,y=75,anchor="w")
        consult_fee = Label(master, text="Scan/Consultation Fee:").place(x=5,y=100,anchor="w")

    def treatment_amount():
        pass

class influenza(sick):          #Child of sick class
    def __init__(self):
        pass

class cancer(sick):             #Child of sick class 
    def __init__(self):
        pass

p1=sick(root)

root.mainloop()
