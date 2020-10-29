#Aashiq Adams 
#Selection sort program

def selection_sort(items):
    #sorts a list of items into ascending order 
    # using the selection sort algorithm
    for step in range(len(items)):
        #Find the location of the smallest element in items[step:]

        for location in range(step, len(items)):
            #To do: determine location of smallest
            if items[location]<items[step]:
                items[location], items[step] = items[step], items[location]
            
    print(items)
        #to do: Exchange items[step] with items[location_of_smallest]


x = []
y = int(input("Enter a number"))
x.append(y)
while True:
    c = int(input("Enter another number, or -1 to stop \n"))
    if c == -1:
        break
    x.append(c)
print(x)
selection_sort(x)


from tkinter import *

root = Tk()

intake = Entry(root, text="")
intake_label = Label(root, text="")


root.mainloop()