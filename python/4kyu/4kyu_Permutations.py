import itertools

def permutations(string):

    #permutaciones = permuta(string)
    permutaciones = itertools.permutations(string,len(string))
    sol = ["".join(i) for i in permutaciones]
    sol = comprobarIguales_(sol)

    return sol

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]

def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def comprobarIguales(arr):
    aux = []
    for i in arr:
        if i not in aux:
            aux.append(i)
    return aux

def comprobarIguales_(arr):
    aux = set()
    for i in arr:
        aux.add(i)
    return aux

if __name__ == '__main__':
    string = "aabbd"
    sol = permutations(string)
    #print("\n\n\n\n\n\n\n")
    print(sol)



'''
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

def permutations(string):
  if len(string) == 1: return set(string)
  first = string[0]
  rest = permutations(string[1:])
  result = set()
  for i in range(0, len(string)):
    for p in rest:
      result.add(p[0:i] + first + p[i:])
  return result

'''


