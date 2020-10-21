from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Sick class")
root.geometry("800x800")
class influenza:
    def __init__(self, master):
        myFrame=Frame(master)
        myFrame.pack()
        self.mysick=Label(master, text="Sickness Code").place(x=10, y=60)
        self.sick_code = Label(master, text="Sickness Code").place(x=10, y=60)
        self.duration_of_Treatment = Label(master, text="Duration of Trament").place(x=10, y=100)
        self.doctors_prac_numberof = Label(master, text="Doctors Practice Number").place(x=10, y=130)
        self.scan_cons_fee = Label(master, text="Scan /Consultation").place(x=10, y=160)
        self.Amount = Label(master, text="Amount paid for treatment").place(x=10, y=190)
        self.Amount_lab = Label(root, width=30).place(x=190, y=190)
        self.myButton = Button(master, text="Calculate", command=self.calculate)
        self.myButton.place(x=400, y=400)

        self.calc_button = Button(root, text="Calculate", command=self.calculate).place(x=50, y=230)
        self.clear_button = Button(root, text="Clear").place(x=150, y=230)
        self.exit_button = Button(root, text="Exit", command=self.exit).place(x=250, y=230)

        #Input boxes
        self.sick_code_input_area = Entry(root, width=30).place(x=170, y=60)
        self.duration_of_Treatment_entry_area = Entry(root, width=30).place(x=170, y=100)
        self.doctors_prac_numberof_input_area = Entry(root, width=30).place(x=170, y=130)
        self.scan_cons_fee_input_area = Entry(root, width=30).place(x=170, y=160)


    def exit(self):
        root.destroy()
    def calculate(self):
        if self.consultation_fee > 600:
            messagebox.showinfo("showinfo", "You got a discount of 2%")
            discount= self.consultation_fee *0.98
            self.treatment=self.medication + discount
            print(self.treatment)
        else:
            messagebox.showinfo("showinfo", "We can treat you")
            self.treatment=self.medication + self.consultation_fee
            #return("The treatment for the patient is", self.treatment)
            print("Total Payment the treatment for the patient is " & str(self.treatment))


p1=influenza(root)
p1.medication=350
p1.consultation_fee=700

root.mainloop()