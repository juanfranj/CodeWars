def spin_words(sentence):
    sol = []
    for i in sentence.split(" "):
        if len(i) >= 5:
           sol.append(i[::-1])
        else:
            sol.append(i)
 
    return " ".join(sol)

if __name__ == '__main__':
    st = "Hey fellow warriors"
    print(spin_words(st))


'''
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
'''