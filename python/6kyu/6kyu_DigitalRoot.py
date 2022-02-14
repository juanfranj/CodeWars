def digital_root(n):
    while len(str(n)) > 1:
        aux = [int(i) for i in str(n)]
        n = sum(aux)
    return n


def main(n):
    res = digital_root(n)
    print(f"El resultado de {n} es {res}")

if __name__ == '__main__':
    n = 493193
    main(n)

'''
Solución optima

def digital_root(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n
'''
