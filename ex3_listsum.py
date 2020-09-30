def sum(x):
    add=0
    for i in x:
        add=add+i
    return add

ages=[2,12,12,14,15,16,16, 17,18, 14, 20, 20]
print("The sum is",sum(ages))
        
sample = [(2,5),(1,2),(4,4),(2,3),(2,1)]

def sort(x):  
    x.sort(key = lambda x: x[1])  
    return x  
  
print(sort(sample))