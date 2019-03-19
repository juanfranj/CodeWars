def tribonacci(signature, n):
    resultado=[]
    for i in range(3):
        resultado.append(signature[i])
    for i in range(n-3):
        a=0
        for j in range(3):
            a=a+signature[j]
        resultado.append(a)
        signature.pop(0)
        signature.append(a)
      
    print(resultado)
    return resultado[:n]