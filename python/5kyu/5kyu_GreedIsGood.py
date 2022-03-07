from collections import Counter

def score(dice):

    juego = Counter("".join([str(i) for i in dice]))
    puntos = 0
    for key, valor in juego.items():
        puntos += puntuar(key, valor)
    return puntos

def puntuar(key, valor):

    dados = {'111':1000, '666':600, '555':500, '444':400,
    '333':300, '222':200, '1':100, '5':50}
    puntos = 0
    while valor > 0:
        if valor >= 3 and dados.get(key*3):
            puntos += dados[key*3]
            valor -= 3
        elif dados.get(key):
            puntos += dados[key]
            valor -= 1
        else:
            valor -= valor         
    return puntos



if __name__ == '__main__':
    jug = [1, 1, 1, 3, 1]
    puntos = score(jug)
    print(puntos)


'''
def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 
'''
