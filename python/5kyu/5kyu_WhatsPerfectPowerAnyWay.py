from time import time
from math import sqrt, log

def isPP(n):

    sol = None
    for i in range(int(n**0.5), 1, -1):
        #if i**2 > n:
            #break
        for j in range(2,n):
            #print(i,j, i**j)
            if i**j == n:
                sol = [i, j]
                return sol
            if i**j >= n:
                break
    return sol

def isPP_(n):
    for b in range(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None


if __name__ == '__main__':
    n = 700000
    inicio = time()
    print("Comienza mi algoritmo:")
    num = 0.25
    power = []
    for i in range(2, n+1):   
        sol = isPP(i)
        if sol is not None:
            power.append(sol)
        if i == n // 4 or i == n // 2 or i == (n*3) // 4 or i == n:
            print(f"Realizado el {int(num*100)}%: {round(time() - inicio,2)} seg")
            num += 0.25
    #print(power)
    print("final de mi algoritmo: ", round(time() - inicio, 2), "seg")

    inicio = time()
    print("\nComienza algoritmo optimo:")
    num = 0.25
    power = []
    for i in range(2, n+1):   
        sol = isPP_(i)
        if sol is not None:
            power.append(sol)
        if i == n // 4 or i == n // 2 or i == (n*3) // 4 or i == n:
            print(f"Realizado el {int(num*100)}%: {round(time() - inicio,2)} seg")
            num += 0.25
    #print(power)
    print("final de algoritmo optimo: ", round(time() - inicio, 2), "seg")