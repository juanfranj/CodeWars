def to_weird_case(string):
    resultado=string.split(" ")
    final=""
    for i in range(len(resultado)):
        cadena=resultado[i]
        for j in range(len(cadena)):
            if j%2==0:
                if j==0:
                    cadena=cadena[j].upper()+cadena[j+1:]
                if j>0 and j<len(cadena):
                    cadena=cadena[:j]+cadena[j].upper()+cadena[j+1:]
                if j==len(cadena):
                    cadena=cadena[:j]+cadena[j].upper()             
        final=final+cadena+" "
    final=final[:(len(final)-1)]
    return final