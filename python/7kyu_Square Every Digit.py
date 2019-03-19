def square_digits(num):
    
    numero="".join(str(num))
    resultado=""
    for i in numero:
        cuadrado=int(i)**2
        resultado=resultado+str(cuadrado)
    return int(resultado) 