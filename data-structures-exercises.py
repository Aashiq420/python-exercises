#EXERCISE 1
#Creating 2 lists of integer values
list_1 = [3, 6, 9, 12, 15, 18, 21]
list_2 = [4, 8, 12, 16, 20, 24, 28]

#Creating a new list from list_1 by cutting every second entry and starting at index 1
new_list_1 = list_1[1::2]
print("Element at odd-index positions from list 1:\n"+str(new_list_1))

#Creating a new list from list_2 by cutting every second entry and starting at index 0
new_list_2 = list_2[0::2]
print("Element at even-index positions from list 2:\n"+str(new_list_2))

#Merging the two new lists
list_3 = new_list_1 + new_list_2
print("Printing final third list:\n"+str(list_3))

#******************************************************************************************
print("\n\n")
#EXERCISE 2
#creating a list of integer values and printing it
List = [54, 44, 27, 79, 91, 41]
print("Original list:",List)

#Creating a variable to store item at index 4 before its deleted
removed = List[4]
del List[4]
print("List after removing element at index 4:",List)

#Inserting deleted item at index 2
List.insert(2,removed)
print("List after adding element at index 2:",List)

#Inserting deleted item at last
List.append(removed)
print("List after adding element at last:",List)

print("\n\n")
#*****************************************************************************************
#EXERCISE 3
#Creating a list and slicing it into chunks of 3 
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_1 = sampleList[0:3]
chunk_2 = sampleList[3:6]
chunk_3 = sampleList[6:9]

#Printing all results, with reversed chunks as well
print("Original list:",sampleList)
print("Chunk 1:",chunk_1)
print("After reversing it:",chunk_1[::-1])
print("Chunk 2:",chunk_2)
print("After reversing it:",chunk_2[::-1])
print("Chunk 3",chunk_3)
print("After reversing it:",chunk_3[::-1])

print("\n\n")
#*****************************************************************************************
#EXERCISE 4
#Creating a list and an empty dictionary to add results to
original_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict_new={}

#For loop to take each index value of list as a key and 
#assigns the count of it as the corresponding value.
#It then adds each key-value pair to a new list
for i in original_list:
    dict_temp = {i:original_list.count(i)}
    dict_new.update(dict_temp)

#Printing solutions
print("Original list:",original_list)
print("Printing count of each item: ",dict_new)

print("\n\n")
#*****************************************************************************************
#EXERCISE 5
#Creating 2 lists with corresponding index entries
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

#creating a set to store info and initialising i to start at 0 
set_soln = set()
i=0

#While loop runs for length of lists
#adds corresponding indexes of list 1 and list 2 to a set
#until the length of the list is reached
while i<len(first_list):
    set_soln.add((first_list[i],second_list[i]))
    i+=1
    if i==len(first_list):
        break
#Printing solutions in a neat manner
print("First List:",first_list)
print("Second List:",second_list)
print("Result is:",set_soln)

print("\n\n")
#*****************************************************************************************
#EXERCISE 6
#Creating sets 1 and 2 and a third set for intersection
set_1 = {65, 42, 78, 83, 23, 57, 29}
set_2 = {67, 73, 43, 48, 83, 57, 29}
set_3 = set()

#FOR loop to look for elements of set 1 in set 2 and adds 
#intersections to a new set
for i in set_1:
    if i in set_2:
        set_3.add(i)

#removing intersections from set 1
new_set_1 = set_1 - set_3

#Printing results
print("First set:",set_1)
print("First set:",set_2)
print("Intersection is:",set_3)
print("First set after removing common elements:",new_set_1)

print("\n\n")
#*****************************************************************************************
#EXERCISE 7
#Creating sets and printing them
firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
print("First set:",firstSet)
print("Second set:",secondSet)
print("\n")

#Creating function to test if set1 is subset of set2
#and return true or false
def isSubset(firstset,secondset):
    counter=0
    for i in firstset:
        if i in secondset and counter<len(firstset)-1:
            counter+=1
            continue
        elif i in secondset and counter==len(firstset)-1:
            return True
            break
        else:
            return False
            break

#Creating a function to test if set 1 is a superset of set 2
#and return true or false
def isSuperset(set1,set2):
    counter_2 = 0
    for i in set1:
        counter_2+=1
        if len(set1)<len(set2):
            return False
        elif i in set2 and counter_2<len(set1)-1:
            continue
        elif i in set2 and counter_2==len(set1)-1:
            return True

#Sending each set in correct order to subset and superset function
#and printing results with a message
print("First set is subset of second set -",isSubset(firstSet,secondSet))
print("Second set is subset of first set -",isSubset(secondSet,firstSet))
print("\n")
print("First set is superset of second set -",isSuperset(firstSet,secondSet))
print("Second set is superset of first set -",isSuperset(secondSet,firstSet))
print("\n")

#Checking if first set is subset of second set in order
#to clear first set
if isSubset(firstSet,secondSet) == True:
    firstSet.clear()
    print("First Set -",firstSet)
print("Second Set -",secondSet)

print("\n\n")
#*****************************************************************************************
#EXERCISE 8
#creating list and dictionary as well as counter for the loop 
#and list the values of the dictionary
#also creating a list to store non-duplicates 
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jim':47, 'Pam':69, 'Angela':76, 'Dwight':97}
save = sampleDict.values()
counter_3 = 0
store_list=[]

#For loop to check if an element of rollNumber is 
# in the list of dictionary values
#if it is, it is added to empty list to compare after
for i in rollNumber:
    if i in save  and counter_3<len(rollNumber):
        counter_3+=1
        store_list.append(i)
        continue
    elif i in save and counter_3==len(rollNumber):
        store_list.append(i)
        break

#printing results
print("After removing unwanted elements from list:",store_list)

print("\n\n")
#*****************************************************************************************
#EXERCISE 9
#Creating a dictionary and converting the non-duplicates into a list
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
val = list(dict.fromkeys(speed.values()))

#Printing results
print(val)

print("\n\n")
#*****************************************************************************************
#EXERCISE 10
#Creating list and converting to dictionary to
#remove duplicates then converting back to a list
sample_values = [87, 45, 41, 65, 94, 41, 99, 94]
sample_values = list(dict.fromkeys(sample_values))

print("Unique items:",sample_values)
tuple_1 = tuple(sample_values)
print("Tuple:",tuple_1)
print("Min:",min(sample_values))
print("Max:",max(sample_values))
