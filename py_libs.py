from datetime import *
from tkinter import *

window = Tk()

today_date = date(2020, 10, 16)
fortnight = timedelta(days = 14)

lb=Listbox(window)

for i in range(1,11):
    today_date+=fortnight
    lb.insert(END, today_date)
    print(today_date,"\n")

lb.pack()

window.mainloop()