def generate_hashtag(s):
    val = validar_cadena(s)
    if not val:
        sol = False
    else:
        sol = s.split(" ")
        for palabras in range(len(sol)):
            if palabras == 0:
                sol[palabras] = '#'+ sol[palabras].capitalize()
            else:
                sol[palabras] = sol[palabras].capitalize()
        sol = "".join(sol)
    return sol

def validar_cadena(s):
    return True if len(s) > 0 and len(s) <= 140 else False

if __name__ == '__main__':
    text = '#'
    sol = generate_hashtag(text)
    print(sol)
'''
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
'''