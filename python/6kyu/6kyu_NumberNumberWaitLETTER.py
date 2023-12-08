import operator

def do_math(s):
    operadores = ["+", "-", "*", "/"]
    orden = [i for i in s if i.isalpha() == True]
    aux = "".join([i for i in s if i.isalpha() == False]).split(" ")
    dic = dict(zip(aux, orden))
    dic_ord = sorted(dic.items(), key = operator.itemgetter(1))
    print(dic_ord)
    operacion = ""
    j = 0
    
    
    for i in range(0, len(dic_ord)):
        if i is not len(dic_ord) -1 :
            operacion += dic_ord[i][0] + operadores[j]
        else:
            operacion += dic_ord[i][0]
        j += 1
        if j == 4:
            j = 0
    res = eval(operacion)
    print(operacion, res)

if __name__ == '__main__':
    s = "24z6 1z23 y369 89z 900b"
    do_math(s)