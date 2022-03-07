def order_weight(strng):
    arr = strng.split(" ")
    suma = []
    for peso in arr:
        aux = 0
        for j in peso:
            aux += int(j)
        suma.append(aux)
    dic = {}
    ind= 0
    for key in suma:
        if key not in dic.keys():
            dic[key] = [arr[ind]]
            ind += 1
        else:
            dic[key].append(arr[ind])
            ind += 1
    sol = []
    for key in sorted(dic.keys()):
        for valor in sorted(dic[key]):
            sol.append(valor)    
    return " ".join(sol)


if __name__ == '__main__':
    s = '' #"11 11 2000 10003 22 123 1234000 44444444 9999"
    sol = order_weight(s)
    print(sol)
    '''
    def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


    def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum

    def order_weight(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    
    return result
    
    '''