def find_uniq(arr):
    aux = {}
    for i in arr:
        if i not in aux.keys():
            aux[i] = 1
        else:
            aux[i] += 1
    n = [key for key in aux.keys() if aux[key] == 1]
    return n[0]

if __name__ == '__main__':
    arr = [ 10, 3, 3, 3, 3 ]
    n = find_uniq(arr)
    print("El unico número es: ", n)
    print(set(arr))
    