def narcissistic(value):
    numero=0
    for i in str(value):
        numero+=int(i)**len(str(value))
    if numero==value:
        return True
    else:
        return False