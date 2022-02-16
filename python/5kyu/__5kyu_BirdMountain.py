def main():
    mountain_ = [
          "^^^^^",
          " ^^^ ",
          "^^^^^"
        ] 
    mountain = [
        "^^^^^       ",     
        "^^^^^       ",   
        "^^^^^       ",
        "            ",            
        "     ^^^^^^^",
        "     ^^^^^^^",
        "     ^^^^^^^",
        "     ^^^^^^^",
        "     ^^^^^^^",
        "     ^^^^^^^",
        "     ^^^^^^^"
        ]   
    peak_height(mountain)
    
def imprimir(imp):
    for i in imp:
        print(i)

def calculoAlturaUno(i, j, filas, columnas, matriz):
    #primer elemento
    h = '^'
    if (j == 0 or j == (columnas-1)) and matriz[i][j] == '^':
        h = '1'
    ##coloca el nivel 1
    elif matriz[i][j] == '^' and j != (columnas-1):
        if (matriz[i][j-1] == ' ') or matriz[i-1][j] == ' ' or matriz[i+1][j] == ' ' or matriz [i][j+1] == ' ':
            h = '1'
    return h

def calculoAlturaSiguiente(i, j, filas, columnas, matriz):
    #primer elemento
    sup = matriz[i-1][j]
    inf = matriz[i+1][j]
    izd = matriz[i][j-1]
    dch = matriz[i][j+1]
    print(f"fila {i-1}:", matriz[i-1])
    print(f"fila {i}:", matriz[i])
    print(f"fila: {i+1}", matriz[i+1])
    print(f"elemento ({i},{j}): {matriz[i][j]}")
    print(f"sup {sup}, izd {izd}, dch {dch}, inf {inf}\n\n")
    h = alturaSuperior(sup, inf, izd, dch)
    

    return h

def alturaSuperior(sup, inf, izd, dch):
    h = '^'
    if sup == izd and sup != '^':
        if dch == '^':
            h = str(int(sup)+1)
            #print(f"sup {sup}, izd {izd}, dch {dch}, altura {h}")
        elif dch == izd:
            h = str(int(sup)+1)
        else:
            h = str(int(sup)-1)
    elif sup != izd and sup != '^' and izd != '^':
        if inf == '^':
            if abs(int(sup) - int(izd)) <= 1 and dch == '^':
                h = str(max([int(sup), int(izd)]))
                #print(f"sup {sup}, izd {izd}, dch {dch}, inf {inf}, h {h}")
            elif inf == '^' and dch != '^':
                 h = str(int(dch)+1)
            else:
                h = str(max([int(sup), int(izd)])-1)
        else:
            h = str(min([int(inf), int(izd)])+1)
            
    return h

def nivel(nivel, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    #print(f"tamaño {filas}x{columnas}")
    #colocar la primera y ultima filas de 1
    for i in [0, filas-1]:
        for j in range(columnas):
            if matriz[i][j] == '^':
                matriz[i][j] = '1'
    for i in range(filas):
        #print(f"fila {i}: {matriz[i]}")
        #coloco la altura uno
        for j in range(columnas):
            #coloca la primera y ultima fila de 1
            #if (i == 0 or i == (filas-1)) and matriz[i][j] == '^':
            #    matriz[i][j] = '1'
            if matriz[i][j] == '^':
                h = calculoAlturaUno(i, j, filas, columnas, matriz)
                matriz[i][j] = h
        #ahora coloco las demas alturas
        for j in range(columnas):
            #h = '^'
            if (i != 0 or i != (filas-1)) and matriz[i][j] == '^':
                h = calculoAlturaSiguiente(i, j, filas, columnas, matriz)
                matriz[i][j] = h


        #print(f"fila {i}: {matriz[i]}")
    return matriz

def convertirMatriz(matriz):
    mat = []
    for i in matriz:
        aux = []
        for j in i:
            aux.append(j)
        mat.append(aux)
    #imprimir(mat)
    #print("elemento 1-8: ", mat[1][9])
    return mat
def pasarString(matriz):
    aux = []
    for i in matriz:
        aux.append(" ".join(i))
    return aux

def convertirEnteros(matriz):
    mat = []
    for fila in matriz:
        aux = []
        for columna in fila:
            if columna != ' ':
                aux.append(int(columna))
            else:
                aux.append(0)
        mat.append(aux)
    return mat

def buscaMaximo(matriz):
    maximo = 0
    for fila in matriz:
        aux = max(fila)
        if aux > maximo:
            maximo = aux
    return maximo

def peak_height(mountain):
    ##imprimir(mountain)
    matriz = convertirMatriz(mountain)
    matriz = nivel('^', matriz)
    imprimir(matriz)
    matrizString = pasarString(matriz)
    imprimir(matrizString)
    #matrizMaxima = convertirEnteros(matriz)
    maximo = 5
    #maximo = buscaMaximo(matrizMaxima)
    #imprimir(matrizMaxima)
    #print("maximo matriz: ", maximo)
    #matriz = pasarString(matriz)
    #imprimir(matriz)
    
    return maximo

if __name__ == '__main__':
    print("\n------------Solución al problema Bird Mountain-----------\n")
    main()
