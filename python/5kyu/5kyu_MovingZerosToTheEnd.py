def move_zeros(array):
    aux = []
    cont = 0
    for i in array:
        if i != 0:
            aux.append(i)
        else:
            cont += 1
    
    for i in range(cont):
        aux.append(0)
    return aux



if __name__ =='__main__':
    array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
    print(array)
    array = move_zeros(array)
    print(array)

'''
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
'''