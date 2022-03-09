from math import sqrt
from time import time

def sum_for_list(lst):
    inicio = time()
    inicio_primo = time()
    primos = calculo_primos(lst)
    print("calculo primo: ", time()-inicio_primo)
    inicio_sol = time()
    sol = suma_primos(primos, lst)
    print("suma_primos: ", time()-inicio_sol)
    #print(len(primos))
    print(time()-inicio)
    return sol

def suma_primos(primos, lst):
    sol = []
    for primo in primos:
        aux = []
        aux_2 = []
        #aux_2 = [suma for suma in lst if suma%primo == 0]
        for suma in sorted(lst):
            if suma%primo == 0:
                aux_2.append(suma)
            #if primo > abs(suma):
                #print(primo, ">", abs(suma))
                #break
        if len(aux_2) > 0:
            aux.append(primo)
            aux.append(sum(aux_2))
            sol.append(aux)

    return sol

def calculo_primos(lst):
    maxi_1 = max([abs(i) for i in lst])
    maxi = maxi_1
    #print(maxi)
    #maxi = primo_maximo(lst) 
    primos = [2]
    for num in range(3, abs(maxi)+1,2):
        primo = es_primo(num)
        if primo:
            primos.append(num)
    return primos

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_div = round(sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True
    #return not any(n % i == 0 for i in range(3, int(n**0.5) + 1, 2))
       
def primo_maximo(lst):  
    if len(lst) >= 2:
        max = sum(sorted(lst, reverse = True)[0:2])
    else:
        max = lst[0]
    return max

if __name__ == '__main__':
    a = [15, 21, 24, 30, 45]
    a1 =  [714397, -410751, -851818, -730629, -461011, 352255, -244128, -262223, -477688, -897742, 569920]
    a2 = [347274, -938387, -205511, -358091, -905651, 22704, -615872, -609883, -799710, -650425, 316669, -438374, -810725]
    sol = sum_for_list(a2)
    print(sol)