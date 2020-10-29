def find_max(number):
    '''
    >>> find_max([1, 2])
    2
    '''
    return max(number)

def descending(x):
    '''
    >>> descending([2, 1, 3])
    [3, 2, 1]

    '''
    y = sorted(x)
    return y[::-1]

x =  [3, 5, 99, 9, 12, 78]
#testing outputs
print(find_max(x))
print(descending(x))