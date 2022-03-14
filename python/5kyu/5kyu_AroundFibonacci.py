def around_fib(n):
    res = fibo(n)
    cont = contadorDigitos(res)
    chuck = cortarCadena(res)
    maxdigit, maxcont = encontrarMaximo(cont)
    return f"Last chunk {chuck}; Max is {maxcont} for digit {maxdigit}"

    
def encontrarMaximo(n):
    maxdig = 0
    maxcont = 0
    for key, value in n.items():
        if value > maxcont:
            maxdig = key
            maxcont = value
        elif value == maxcont:
            if maxdig > key:
                maxdig = key
                maxcont = value

    return maxdig, maxcont

def cortarCadena(n):
    aux = []
    cont = 1
    res = ''
    if len(str(n)) <= 25:
        aux.append(n)
    else:
        for i in str(n):
            if cont < 25:
                res += i
                cont += 1
            else:
                res += i
                aux.append(res)
                cont = 1
                res = ''
        if len(res) > 0:
            aux.append(res)
 
    return aux[-1]

def fibo(n):
    aux = [0,1]
    if n <= 1:
        if n < 1:
            aux[1] = 0
    else: 
        for i in range(n-1):
            aux.append(aux[-1] + aux[-2])
    return aux[-1]

def contadorDigitos(n):
    res = {}
    for i in str(n):
        if i not in res.keys():
            res[i] = 1
        else:
            res[i] += 1
    return res

if __name__ == '__main__':
    n = 666
    res = around_fib(n)
    print(res)
    

'''
def around_fib(n):
    a, b = 0, 1
    for i in range(n-1): a, b = b, a + b
    fib = str(b)
    lst = len(fib) % 25
    if lst == 0: 
        lst = 25
    maxcnt = 0; digit = -1

    for i in '0123456789':
        c = fib.count(i)
        if c > maxcnt:
            maxcnt = c
            digit = i
    return "Last chunk {}; Max is {} for digit {}".format(fib[-lst:], maxcnt, digit)
'''