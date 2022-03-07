from collections import Counter

def duplicate_encode(word):
    dic = Counter(word.lower())
    text = ''
    for letra in word.lower():
        if dic[letra] > 1:
            text += ')'
        else:
            text += '('
    return text

if __name__ == '__main__':
    s = 'recede'
    print(duplicate_encode(s))
    