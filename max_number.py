#Function to find the max number in a list
#doctest testing is done within the function

def find_max(number):
    '''
    >>> find_max([1, 2])
    2
    '''
    return max(number)

#Function to sort a list in descending order 
#doctest testing is done within the function
def descending(x):
    '''
    >>> descending([2, 1, 3])
    [3, 2, 1]

    '''
    y = sorted(x)
    return y[::-1]

#Testing outputs
x =  [3, 5, 99, 9, 12, 78]
print(find_max(x))
print(descending(x))