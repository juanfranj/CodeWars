def create_spiral(n):
    
    continuar = comprobar(n)
    if not continuar:
        return []
    mat = crear_matriz(n)
    lim = {"lim_sup":0, "lim_inf":n, "lim_izd":0, "lim_dch":n}
    cont = 1
    while True:
        for i in range(lim['lim_izd'], lim['lim_dch']):
            mat[lim['lim_sup']][i] = cont
            cont +=1
        #print(mat)
        if cont == (n*n):
            return mat
        
        for i in range(lim['lim_sup']+1, lim['lim_inf']):
            mat[i][lim['lim_dch']-1] = cont
            cont +=1
        #print(mat)
        if cont == (n*n)+1:
            return mat
        
        for i in range(lim['lim_dch']-2, lim['lim_izd']-1, -1):
            mat[lim['lim_inf']-1][i] = cont
            cont += 1
        #print(mat)
        if cont == (n*n)+1:
            return mat
        
        for i in range(lim['lim_inf']-2, lim['lim_sup'],-1):
            mat[i][lim['lim_izd']] = cont
            cont += 1
        #print(mat)
        if cont == (n*n)+1:
            return mat
        actualizar_limites(lim)
          
def crear_matriz(n):

    mat = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(0)
        mat.append(aux)
    return mat

def actualizar_limites(lim):

    lim['lim_sup'] += 1
    lim['lim_inf'] -= 1
    lim['lim_izd'] += 1
    lim['lim_dch'] -= 1
    
def comprobar(n):
    continuar = True
    if not isinstance(n,int) or n<1:
        continuar = False
    return continuar
    

if __name__ == '__main__':
    n = 15
    mat = create_spiral(n)
    for i in mat:
        print(i)
    

'''
def createSpiral(n):
    if not isinstance(n, int): return []
    d = iter(range(n ** 2))
    a = r = [[[x, y] for y in range(n)] for x in range(n)]
    while a:
        for x, y in a[0]: r[x][y] = next(d) + 1
        a = list(zip(*a[1:]))[::-1]
    return r

def createSpiral(n):
    if not isinstance(n,int) or n<1:
        return []
    seq = list(range(1,n**2))
    arr = [[n**2]]
    while seq:
        l = len(arr)
        arr = [seq[-l:]] + list(map(list, zip(*arr[::-1])))
        seq = seq[:-l]
    return arr

'''