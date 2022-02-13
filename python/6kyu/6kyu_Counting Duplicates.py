import re
def duplicate_count(text):
    cont=0
    text=text.replace("\"","")
    text=text.lower()
    repetidas=""
    for i in text:
        if len(re.findall(i,text))>1:
            repetidas=repetidas+i
            if len(re.findall(i,repetidas))==1:
               cont=cont+1
    return cont