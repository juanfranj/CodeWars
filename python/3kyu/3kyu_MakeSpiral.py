def spiralize(n):
    
    continuar = comprobar(n)
    if not continuar:
        return []
    mat = crear_matriz(n)
    lim = {"lim_sup":0, "lim_inf":n, "lim_izd":0, "lim_dch":n}
    cont = 0
    #print(contador(n))
    while True:
        #print(cont)
        for i in range(lim['lim_izd']-1, lim['lim_dch']):
            mat[lim['lim_sup']][i] = 1
            cont +=1
        #imprimir(mat)
        if cont > contador(n):
            return mat
        
        for i in range(lim['lim_sup']+1, lim['lim_inf']):
            mat[i][lim['lim_dch']-1] = 1
            cont +=1
        #imprimir(mat)
        if cont > contador(n):
            return mat
        
        for i in range(lim['lim_dch']-2, lim['lim_izd']-1, -1):
            mat[lim['lim_inf']-1][i] = 1
            cont += 1
        #imprimir(mat)
        if cont > contador(n):
            return mat
        
        for i in range(lim['lim_inf']-2, lim['lim_sup']+1,-1):
            mat[i][lim['lim_izd']] = 1
            cont += 1
        #imprimir(mat)
        if cont > contador(n):
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

    lim['lim_sup'] += 2
    lim['lim_inf'] -= 2
    lim['lim_izd'] += 2
    lim['lim_dch'] -= 2
    
def comprobar(n):
    continuar = True
    if not isinstance(n,int) or n<1:
        continuar = False
    return continuar
  
def contador(size):
    
    return size**2//2 + size if size % 2 else size**2//2 + (size - 1)

def imprimir(mat):
    print()
    for i in mat:
        print(i)

if __name__ == '__main__':
    n = 12
    mat = spiralize(n)
    imprimir(mat)

'''
def spiralize(size):
    
    def on_board(x, y):
        return 0 <= x < size and 0 <= y < size
        
    def is_one(x, y):
        return on_board(x, y) and spiral[y][x] == 1
        
    def can_move():
        return on_board(x+dx, y+dy) and not (is_one(x+2*dx, y+2*dy) or is_one(x+dx-dy, y+dy+dx) or is_one(x+dx+dy, y+dy-dx))
    
    
    spiral = [[0 for x in range(size)] for y in range(size)]   
    x, y = -1, 0
    dx, dy = 1, 0
    turns = 0
    
    while (turns < 2):
        if can_move():
            x += dx
            y += dy
            spiral[y][x] = 1
            turns = 0
        else:
            dx, dy = -dy, dx
            turns += 1
    
    return spiral

def spiralize(size):
    # Make a snake
    spiral = [[1 - min(i,j,size-max(i,j)-1)%2 for j in xrange(size)] for i in xrange(size)]
    for i in xrange(size/2-(size%4==0)):
      spiral[i+1][i] = 1 - spiral[i+1][i]
    return spiral

'''