"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]

"""

"""
Best solution:

def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []

def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a
"""

def snail(array):
    a = np.array(array)
    fin = False
    solucion=[]
    cont=0
    while not fin:
        for i in a[0][:]:
            solucion.append(i)
        a = np.rot90(a[1:,:])
        cont +=1
        if a.shape[1] == 0:
            fin = True
    return solucion
