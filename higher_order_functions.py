# Exercise 1:
# grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
# Task:
# Filter the grades to only display everyone above (and including) 70%

#creating grades list and empty list to 
#append grades to be displayed
grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
display = []

#for loop to go through list and add any grades 
#above and equal to 70 to the display list
for i in grades:
    if i>=70:
        display.append(i)
print("Grades:",grades)
print("Grades 70 and above:",display)
print("\n")


# Exercise 2:
# dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]
# Task:
# Convert the ages into "dog years" (x7)

#Creating a list to store dogs ages
#and a list to store converted ages
dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]
dog_years = []

#For loop to take each entry in dog_ages and 
#multiply it by 7, then add to dog_years to be displayed
for i in dog_ages:
    dog_years.append(i*7)

print("Dog ages in human years:",dog_ages)
print("Dog ages in dog years:",dog_years)
print("\n")


# Exercise 3:
# transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.49]
# Task:
# Convert the transactions to a single total

#Creating list of transactions
transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.49]

#printing the list as well as the sum of the list
print("Transactions:",transactions)
print("The total is:",sum(transactions))