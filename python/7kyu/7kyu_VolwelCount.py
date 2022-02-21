def get_count(sentence):
    cont = 0
    for i in sentence:
        if i in r'[aeiou]':
            cont += 1
    return cont

def get_count_(sentence):
    return sum([1 for i in sentence if i in r'[aeiou]'])

if __name__ == '__main__':
    sentence = 'aeiou'
    sol = get_count(sentence)
    print(sol)
    sol = get_count_(sentence)
    print(sol)