def valid_parentheses(string):
    contador=0
    for i in string: 
        if i=="(": contador+=1
        if i==")": contador-=1
        if contador<0: break
    if contador==0: return True
    else: return False