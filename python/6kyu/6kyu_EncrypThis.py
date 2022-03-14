def encrypt_this(text):
    texto=text.split(" ")
    solucion=[]
    for i in texto:
        palabra=""
        i.replace(" ","")
        if len(i)==0: continue
        if len(i)==1: palabra+=str(ord(i[0]))
        if len(i)==2: palabra+=str(ord(i[0]))+i[-1]
        if len(i)>2: palabra=str(ord(i[0]))+i[-1]+i[2:len(i)-1]+i[1]
        solucion.append(palabra)
    return " ".join(solucion)