import re
def increment_string(strng):
    num="".join(re.findall(r"\d+\b$",strng))
    if len(num)==0:
        num="0"
    palabra=strng.replace(num,"")
    longitud=len(num)
    actualizacion=str(int(num)+1)
    lonAct=len(str(actualizacion))
    if longitud>lonAct:
        for i in range(longitud-lonAct):
            palabra+="0"
        actualizacion=list(actualizacion)
        actualizacion="".join(actualizacion)
    strng=palabra+actualizacion
    return strng