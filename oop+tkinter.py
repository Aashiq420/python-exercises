from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Aashiq's Program")
root.geometry("600x400")

#Parent class of influenza and cancer classes
class sick:                     
    def __init__(self):
        pass
    def calculate(x, y):
        print(x)
        if y == 0:
            print("cancer")
            run = cancer(x)
        elif y == 2:
            print("flu")
            run = influenza(x)
        else:                           #error check print
            print("error somewhere bro")
    
    #labels
    sickness_code = Label(root, text="Sickness Code:").place(x=25,y=50,anchor="w")
    treatment_duration = Label(root, text="Duration of Treatment:").place(x=25,y=100,anchor="w")
    duration_unit = Label(root, text="Weeks/Months").place(x=390, y=88)
    doc_prac_num = Label(root, text="Doctor's Practice Number:").place(x=25,y=150,anchor="w")
    consult_fee = Label(root, text="Scan/Consultation Fee:").place(x=25,y=200,anchor="w")
    amount_paid_label = Label(root, text="Amount paid for treatment:").place(x=25,y=300)
    amount_paid_display = Label(root, text=">placeholder<").place(x=225,y=300)

    #entry boxes
    sick_id = Entry(root).place(x=300, y=35)
    duration = Entry(root, width=10).place(x=300, y=85)
    doc_id = Entry(root).place(x=300, y=135)
    scan_or_consult = Entry(root).place(x=300, y=185)
    
    #radiobuttons
    v = IntVar()
    cancer_radio = Radiobutton(root, text="Cancer", variable=v, value=1).place(x=20, y=230)
    influenza_radio = Radiobutton(root, text="Influenza", variable=v, value=2).place(x=20, y=260)
    print(v.get()) #integer value

    #calculate and clear button
    clear = Button(root, text="Clear").place(x=225, y=350)
    calc = Button(root, text="Calculate", command=calculate(scan_or_consult, v)).place(x=25, y=350)
    


#Child of sick class 
class cancer(sick):            
    def __init__(self, scan):
        amount_paid_display = Label(root, text="")
        amount_paid_display.place(x=225,y=300)
        medication = 400
        self.scan = scan
        print(scan)
        if int(scan)>600:
            messagebox.showinfo("Message", "Sorry we cannot treat you")
        else:
            amount_paid = int(scan) + medication
            amount_paid_display.config(text="R"+str(amount_paid))

#Child of sick class
class influenza(sick):          
    def __init__(self, consult):
        amount_paid_display = Label(root, text="")
        amount_paid_display.place(x=225,y=300)
        medication = 400
        self.consult=consult
        print(consult)
        if consult>600:
            consult = 0.98*consult
            amount_paid = float(consult) + medication
            amount_paid_display.config(text="R"+str(amount_paid))
        else:
            amount_paid = medication+float(consult)
            amount_paid_display.config(text="R"+str(amount_paid))


p1=sick()

root.mainloop()
