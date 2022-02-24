import itertools

def mix(s1, s2):
    s1 = contar_letras(s1)
    s2 = contar_letras(s2)
    s = encontrar_maximos(s1, s2)
    text = imprimir_cadena(s)
    return text

def contar_letras(s):
    dic = {}
    for key in s:
        if key >= 'a' and key <= 'z':
            if key not in dic.keys():
                dic[key] = 1
            else:
                dic[key] += 1
    return dic

def encontrar_maximos(s1, s2):
    dic = {}
    for key_1, key_2 in itertools.zip_longest(s1.keys(), s2.keys()):
        if key_1 in s2.keys() and max(s1[key_1], s2[key_1]) > 1:
            dic[key_1] = max(s1[key_1], s2[key_1])
        if key_1 not in s2.keys() and key_1 != None and s1[key_1] > 1:
            dic[key_1] = s1[key_1]
        if key_2 not in s1.keys() and key_2 != None and s2[key_2] > 1:
            dic[key_2] = s2[key_2]
    dic = buscar_indices(s1, s2, dic)
    dic = ordenar_diccionario(dic)
    return dic

def ordenar_diccionario(dic):
    lista = sorted(dic.items(), key=lambda kv: (-kv[1][0], kv[1][1], kv[0]))
    aux = {}
    for key, valor in lista:
        aux[key] = valor
    return aux

def buscar_indices(s1, s2, s):
    for key in s.keys():
        if key in s1.keys() and key in s2.keys():
            if s1[key] > s2[key]:
                s[key] = (s[key], '1')
            elif s1[key] < s2[key]:
                s[key] = (s[key], '2')
            else:
                s[key] = (s[key], '=')
        elif key in s1.keys():
            s[key] = (s[key], '1')
        else:
            s[key] = (s[key], '2')
    return s

def imprimir_cadena(s):
    text = ''
    for key, value in s.items():
        text += value[1] + ':' +key * value[0] + '/'
    return text[:-1]

if __name__ == '__main__':
    s1 = " lkjasljoioajf aojflalkalajf aljaflkajfoafsdofalkjf lfkjalkjaljkafjfa fahiuqewiuyorhwnfvknn nflafldjoiewfn,"
    s2 = " oiweqoriljeqwrlkgfn flasdflkjfdsoiqwer ewlfkjalskfdjlfsaj qweqwherqiewuhriewur afsalkkfdjfs qwehrhjqerwoafoafpg`lk"
    sol = mix(s1, s2)
    print(sol) #"1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    
'''
from collections import Counter

def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))
 
'''