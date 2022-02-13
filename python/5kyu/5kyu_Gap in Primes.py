def gap(g, m, n):
    primos=[]
    resul=[]
    cont=0
    for i in range(m,n):
        if g>10: break
        if i == 1 or i==2: 
            primos.append(i)
            cont+=1
        else:
            for j in range(2,int(i ** 0.5) + 1):
                if i%j==0: 
                    esPrimo=False
                    break
                else: esPrimo=True
            if esPrimo:
                primos.append(i)
                cont+=1 
            if cont>=2:
                if primos[cont-1]-primos[cont-2]==g:
                    resul.append(primos[cont-1])
                    resul.append(primos[cont-2])
                    #print(cont,primos)
                    return resul[::-1]