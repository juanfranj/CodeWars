def anagrams(word, words):
    sol = []
    word = convertir_diccionario(word)
    for i in words:
        dic = convertir_diccionario(i)
        estado = comprobar_anagrama(dic, word)
        if estado:
            sol.append(i)
    return sol
        
def comprobar_anagrama(dic, word):
    estado = True
    for key, value in dic.items():
        if key not in word.keys() or word[key] != value:
            estado = False
            break
    return estado

def convertir_diccionario(word):
    dic = {}
    for i in word:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    return dic


if __name__ == '__main__':
    word = 'racer'
    words = ['crazer', 'carer', 'racar', 'caers', 'racer']
    sol = anagrams(word, words)
    print(f"Las palabras anagramas de {words} con {word} son:\n{sol}")

    sol = []
    for i in words:
        if sorted(i) == sorted(word):
            sol.append(i)
    print(f"Las palabras anagramas de {words} con {word} son:\n{sol}")


'''
def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]
'''