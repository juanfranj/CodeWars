def sum_of_intervals(intervals):
    maximo = 0
    for i in intervals:
        for j in i:
            if j > maximo: maximo = j
    a = [1 for i in range(maximo)]
    cont = 0
    for i in intervals:
        for j in range(i[0], i[1]):
            if a[j] == 1:
                cont += 1
                a[j] = 0
    return cont