from itertools import zip_longest


def same_structure_as(original,other):
    if isinstance(original, list) != isinstance(other, list):
        return False
    igual = [True]
    igual = comprobar_estructura(original, other, igual)
    return igual

def comprobar_estructura(original, otra, sol):
    
    for elemento_original, elemento_otra in zip_longest(original, otra):
        if isinstance(elemento_original, list) and isinstance(elemento_otra, list) and len(elemento_original) == len(elemento_otra):
            comprobar_estructura(elemento_original, elemento_otra, sol)  
        elif isinstance(elemento_original, list) != isinstance(elemento_otra, list):
            sol.append (False)
        elif isinstance(elemento_original, list) and isinstance(elemento_otra, list) and len(elemento_original) != len(elemento_otra):
            sol.append (False)
        else:
            sol.append(True)
    return False if False in sol else True



if __name__ == '__main__':
    original = []
    other = 1
    sol = same_structure_as(original, other)
    print(sol)

'''
def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)

def same_structure_as(a, b):
    return (False if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b)
            else all(same_structure_as(c, d) for c, d in zip(a, b) if isinstance(c, list)))
'''