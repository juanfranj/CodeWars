
def sort_nested_list(A):
    ord =[]
    ord = sorted(extraer_elementos(A, ord))
    introducir_elemento(A, ord)
    return A

def introducir_elemento(A, ord): 
    for elemento in range(len(A)):
        if isinstance(A[elemento], list):
            introducir_elemento(A[elemento], ord)
        else:
            A[elemento] = ord.pop(0)

def extraer_elementos(lista, sol):
    for elemento in lista:
        if isinstance(elemento,list):
            extraer_elementos(elemento, sol)
        else:
            sol.append(elemento)
    return sol
            
if __name__ == '__main__':
    A=[[[82, 87], [47, 44]], [[70, 94], [40, 64]]]
    sol = sort_nested_list(A)
    print(sol)

    '''
    def sort_nested_list(xsss):
    ys = iter(sorted(x for xss in xsss for xs in xss for x in xs))
    return [[[next(ys) for x in xs] for xs in xss] for xss in xsss]
    '''