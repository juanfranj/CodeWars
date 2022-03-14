"""
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
"""
"""
Best Code

def validateBattlefield(field):
    n, m = len(field), len(field[0])
    def cell(i, j):
        if i < 0 or j < 0 or i >= n or j >= m: return 0
        return field[i][j]
    def find(i, j):
        if cell(i + 1, j - 1) or cell(i + 1, j + 1): return 10086
        if cell(i, j + 1) and cell(i + 1, j): return 10086
        field[i][j] = 2
        if cell(i, j + 1): return find(i, j + 1) + 1
        if cell(i + 1, j): return find(i + 1, j) + 1
        return 1
    num = [0] * 5
    for i in xrange(n):
        for j in xrange(m):
            if cell(i, j) == 1:
                r = find(i, j)
                if r > 4: return False
                num[r] += 1
    [tmp, submarines, destroyers, cruisers, battleship] = num
    return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4

"""
import numpy as np

def buscarBarco(field,resultado):
    x = 0
    y = 0
    cont = 0
    for i in range(10):
        for j in range(10):
            if field[i][j] == 1:
                x = i
                y = j
                cont +=1
                return x, y, resultado
    if cont == 0:
        return x, y, resultado            
    
def comprobarBarco(field, x, y):
    tamaño_X = 0
    tamaño_Y = 0
    tamaño = 0
    fin = False
    coordenadas_X = []
    coordenadas_Y = []
    coordenadas = []
    # Busco en la coordenada x
    i = x
    j = y
    while not fin:
        if i < 10:
            if field[i][j] == 1:
                coordenadas_X.append([i, j])
                tamaño_X += 1
                i += 1
            else:
                fin = True
        else:
            fin =True
    # Busco en la coordenada y
    fin = False
    i = x
    j = y
    while not fin:
        if j < 10:
            if field[i][j] == 1:
                coordenadas_Y.append([i, j])
                tamaño_Y += 1
                j += 1
            else:
                fin = True
        else:
            fin = True
    # Compruebo el tamaño del barco
    if tamaño_X > tamaño_Y:
        tamaño = tamaño_X
        coordenadas = coordenadas_X
    elif tamaño_Y > tamaño_X:
        tamaño = tamaño_Y
        coordenadas = coordenadas_Y
    else:
        tamaño = tamaño_X
        coordenadas = coordenadas_X 
    return tamaño, coordenadas

def actualizarField(field, coordenadas):
    for i in range(len(coordenadas)):
        x, y = coordenadas[i]
        field[x][y] = 0
    return field

def actualizarJuego(tamaño,juego):
    tamañoBarcos = {4:"battleship", 3:"cruiser", 2:"destroyer", 1:"submarine"}
    fin = False
    resultado = True
    if tamaño in tamañoBarcos:
        barco = tamañoBarcos[tamaño]
    else:
        barco = "No existe"
        fin = True
        resultado = False
        return fin, resultado, juego
    numeroBarcos = juego[barco]-1
    if numeroBarcos < 0:
        fin = True
        resultado = False
        return fin, resultado, juego
    juego[barco] = numeroBarcos
    return fin, resultado, juego

def comprobarContacto(field, coordenadas):
    fin = False
    resultado = True
    x = []
    y = []
    for i, j in coordenadas:
        x.append(i)
        y.append(j)
    xMin = min(x)
    xMax = max(x)
    yMin = min(y)
    yMax = max (y)
    # Barco Vertical
    if yMin == yMax:
        for i in range(xMin-1,xMax+2):
            if i >= 0 and i < 10 and yMin+1 < 10:
                if field[i][yMin+1] != 1:
                    field[i][yMin+1] = 3
                else:
                    fin = True
                    resultado = False
                    break
            if i >= 0 and i < 10 and yMin-1 >= 0:
                if field[i][yMin-1] != 1:
                    field[i][yMin-1] = 3
                else:
                    fin = True
                    resultado = False
                    break
    # Barco Horizontal
    if xMin == xMax:
        for i in range(yMin-1, yMax+2):
            if i >= 0 and i < 10 and xMin+1 < 10:
                if field[xMin+1][i] != 1:
                    field[xMin+1][i] = 3
                else:
                    fin = True
                    resultado = False
                    break
            if i >= 0 and i < 10 and xMin-1 >= 0:
                if field[xMin-1][i] != 1:
                    field[xMin-1][i] = 3
                else:
                    fin = True
                    resultado = False
                    break
    return fin, resultado, field

def validate_battlefield(field):
    field = np.array(field)
    juego = {"battleship":1, "cruiser":2, "destroyer":3, "submarine": 4}
    fin = False
    resultado = True
    cont = 0
    while cont < 10 and fin == False:
        x, y, resultado = buscarBarco(field,resultado)
        tamaño, coordenadas = comprobarBarco(field, x, y)
        field = actualizarField(field, coordenadas)
        fin, resultado, juego = actualizarJuego(tamaño,juego)
        if resultado == False or fin == True: break 
        fin, resultado, field = comprobarContacto(field, coordenadas)       
        cont += 1
    x, y, resultado = buscarBarco(field,resultado)
    if sum(juego.values()) != 0 or x != 0 or y !=0: 
        resultado = False    
    return resultado