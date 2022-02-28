def max_sequence(arr):
    arr = comprobar(arr)
    sub_arr = encontrar_subarrays(arr)
    #imprimir(sub_arr)
    suma = [sum(i) for i in sub_arr]
    suma_maxima = sub_arr[suma.index(max(suma))]
    #imprimir(suma)
    return sum(suma_maxima) if sum(suma_maxima) >=0 else 0

def comprobar(arr):
    return [0] if len(arr) == 0 else arr   

def encontrar_subarrays(ar):
    arr =[]
    for i in range(len(ar)):
        aux = []
        for j in range(i, len(ar)):
            aux.append(ar[j])
            a = aux[::]
            arr.append(a)        
    return arr

def imprimir(arr):
    for i in arr:
        print(i)

if __name__ == '__main__':
    ar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ar1 = []
    ar2 = [-2, -1, -3]
    sol = max_sequence(ar2)
    print(sol)


'''
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
'''