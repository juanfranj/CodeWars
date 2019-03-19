import time
import re
def interpreter(code, tape):
    codigo=list(code)
    cadena=list(tape)
    posicion=0
    i=0
    posicionCorchete=[]
    longitudCodigo=len(codigo)
    longitudCadena=len(cadena)
    start=time.time()
    while i<longitudCodigo:
        if codigo[i]=="*":
            if cadena[posicion]=="0": 
                cadena[posicion]="1" 
                i+=1
            else: 
                cadena[posicion]="0" 
                i+=1        
        elif codigo[i]==">":
            if posicion<longitudCadena-1:
                posicion+=1
                i+=1
            else: return "".join(cadena)
        elif codigo[i]=="<":# and posicion!=0:
            if posicion!=0:
                posicion-=1
                i+=1
            else: return "".join(cadena)
        elif codigo[i]=="[" and cadena[posicion]!="0":
            posicionCorchete.append(i)
            i+=1
        elif codigo[i]=="[" and cadena[posicion]=="0":
            corchete=1
            posicionCorchete.append(i)
            i+=1
            for t in range(i,len(codigo)):
                if codigo[t]!="]" and codigo[t]!="[":
                    i+=1
                if codigo[t]=="[":
                    posicionCorchete.append(i)
                    corchete+=1
                    i+=1
                if codigo[t]=="]" and corchete>1:
                    i+=1
                    corchete-=1
                    posicionCorchete.pop()
                elif codigo[t]=="]" and corchete==1:
                    break
        elif codigo[i]=="]" and cadena[posicion]!="0": 
            i=posicionCorchete[-1]
        elif codigo[i]=="]" and cadena[posicion]=="0": 
            i+=1
            posicionCorchete.pop()
        elif re.search(r"[,.;:!¿?+%-><nsew^$#@\s\w]",codigo[i])!=None: i+=1
        final=time.time()
        if final-start>0.1: return "Tiempo excedido"
    return "".join(cadena)