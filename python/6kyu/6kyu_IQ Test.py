def iq_test(numbers):
    numeros=numbers.split(" ")
    par=[]
    impar=[]
    for i in numeros:
        if int(i)%2: par.append(i)
        else: impar.append(i)
    if len(par)<len(impar): indice=numeros.index(par[0])
    else: indice=numeros.index(impar[0])
    return indice+1