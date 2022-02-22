from itertools import  combinations
from time import time

#variable global del script

teclado = (['*','*','*','*','*'],
            ['*','1','2','3','*'],
            ['*','4','5','6','*'],
            ['*','7','8','9','*'],
            ['*','*','0','*','*'],
            ['*','*','*','*','*']
            )

def get_pins(observed):
    inicio = time()
    num = list(str(observed))
    pos = []
    for i in num:
        pos.append(posibles_numeros(i))
    lista = encontrar_permutaciones(pos, len(num))
    print(f"Fin de permutacion: {time()-inicio}")
    inicio1 = time()
    pins = validar_numeros(lista, pos, len(num))
    print(f"Fin de validacion: {time()-inicio1}")
    print(f"Fin de Software: {time()-inicio}")
    return pins


def validar_numeros(numeros,pos, lon):
    cont = 0
    for i in pos:
        for numero in numeros:
            if numero[cont] not in i:
                numeros[numeros.index(numero)] = "*" * lon    
        cont += 1
    return [i for i in numeros if '*' not in i]
  
def encontrar_permutaciones(pos, lon):
    lista = []
    for i in pos:
        lista.extend(i)
    lista = ["".join(i) for i in set(combinations(lista, lon))]
    return lista   

def posibles_numeros(num):
    posib = []
    x, y = posicion(num)
    for i in range((x-1), (x+2), 2):
        posib.append(teclado[i][y])
    for i in range((y-1), (y+2)):
        posib.append(teclado[x][i])
    posib = [i for i in posib if i != '*']

    return posib

def posicion(num):

    for i in range(5):
        for j in range(5):
            if num in teclado[i][j]:
                break
        else:
            continue
        break
    return i, j


if __name__ == '__main__':

    pin = '123654'
    sol = get_pins(pin)
    print(sol)
    #print(["".join(i) for i in set(combinations(['8','0','8','0','8','0', '8','0', '8','0', '8','0', '8','0', '8','0'], 8))])
    
'''
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
'''
    