import operator
def order(sentence):
    dic = pasar_diccionario(sentence)
    sort = sorted(dic.items(), key = operator.itemgetter(1))
    #print([i[0] for i in sort])
    return " ".join([i[0] for i in sort])

def pasar_diccionario(s):
    dic = {}
    for i in s.split(" "):
        for j in range(1, len(s.split(" "))+1):
            print(i, j)
            if str(j) in i:
                dic[i] = j
                break
    return dic

if __name__ == '__main__':
    s = "4of Fo1r pe6ople g3ood th5e the2"
    print(order(s))

'''
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))


def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
'''