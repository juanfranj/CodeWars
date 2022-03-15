def done_or_not(board):
    valid = True
    #compruebo filas
    for i in board:
        fila = i
        valid = validar(fila)
        if valid is False:
            return 'Try again!'
    #compruebo columnas
    for j in range(9):
        col = []
        for i in range(9):
            col.append(board[i][j])
        valid = validar(col)
        if valid is False:
            return 'Try again!'
    #compruebo rectangulos
    arr = [[0, 2, 0, 2], 
            [0, 2, 3, 5],
            [0, 2, 6, 8],
            [3, 5, 0, 2], 
            [3, 5, 3, 5],
            [3, 5, 6, 8],
            [6, 8, 0, 2], 
            [6, 8, 3, 5],
            [6, 8, 6, 8],
            ]
    for i0, i1, j0, j1 in arr:
        cuad = []
        for i in range(i0, i1+1):
            for j in range(j0, j1+1):
                cuad.append(board[i][j])
        valid = validar(cuad)
        if valid is False:
            return 'Try again!'
    return 'Finished!'

def validar(arr):
    aux = {}
    for i in arr:
        if i not in aux.keys():
            aux[i] = 1
        else:
            aux[i] += 1
    valid = comprobar(aux)
    return valid

def comprobar(dic):
    
    valid = True
    if 0 in dic.keys():
            valid = False
    else: 
        for i in range(1,10):
            if i not in dic.keys():
                valid = False
        for value in dic.values():
            if value > 1:
                valid = False
    return valid

            
        


if __name__ == '__main__':
    sudo = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    res = done_or_not(sudo)
    print(res)


'''
import numpy as np
def done_or_not(aboard): #board[i][j]
  board = np.array(aboard)

  rows = [board[i,:] for i in range(9)]
  cols = [board[:,j] for j in range(9)]
  sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
  
  for view in np.vstack((rows,cols,sqrs)):
      if len(np.unique(view)) != 9:
          return 'Try again!'
  
  return 'Finished!'
'''