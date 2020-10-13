from tkinter import *
from tkinter import ttk

window_1 = Tk()

#single line text-box
window_1.geometry("400x250")
name = Label(window_1, text = "Name").place(x = 30, y = 50)
email = Label(window_1, text = "User ID").place(x = 30, y = 90)
password =  Label(window_1, text = "Password").place(x = 30, y = 130)
sbmitbtn = Button(window_1, text = "Submit", activebackground = "green", activeforeground = "blue").place(x = 120, y = 170)
entry1 = Entry(window_1).place(x = 85, y = 50)
entry2 = Entry(window_1).place(x = 85, y = 90)
entry3 = Entry(window_1).place(x = 90, y = 130)

#hello button
hello = Button(window_1, text="Hello")
hello.pack()

#exit button
exit_btn = Button(window_1, text="Exit")
exit_btn.pack()

#canvas
canvas_1 = Canvas(window_1, width=200, height=100)
canvas_1.pack()

#combobox
combobox = ttk.Combobox(window_1, values=["Strawhat","Red haired","Blackbeard"])
combobox.pack()

#checkbutton
check = Checkbutton(window_1, text="Conquerer haki")
check.pack()

#spinbox
spin= Spinbox(window_1, from_=0, to=10)
spin.pack()

#text widget
text_widget =Text(window_1)
text_widget.insert('1.0', "- Hello there, Kenobi-")
text_widget.insert('1.14', ' General')
text_widget.delete('1.0')
text_widget.delete('end - 2 chars')
text_widget.pack()

#radio buttons
v = IntVar()

radio_btn_1 = Radiobutton(window_1, text="One", variable=v, value=1).pack(anchor=W)
radio_btn_2 = Radiobutton(window_1, text="Two", variable=v, value=2).pack(anchor=W)

window_1.mainloop()