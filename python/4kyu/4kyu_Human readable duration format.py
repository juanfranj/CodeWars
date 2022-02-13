def format_duration(seconds):
    duracion=[0,0,0,0,seconds]
    constantes=[60*60*24*365,60*60*24,60*60,60]
    escritura=[]
    if duracion[4]==0:
        escritura.append("now")
    if duracion[4]/constantes[0]>=1:
        duracion[0]=int(duracion[4]/constantes[0])
        duracion[4]=duracion[4]-duracion[0]*constantes[0]
        if duracion[0]==1: escritura.append(str(duracion[0])+" year")
        else: escritura.append(str(duracion[0])+" years")
    if duracion[4]/constantes[1]>=1:
        duracion[1]=int(duracion[4]/constantes[1])
        duracion[4]=duracion[4]-duracion[1]*constantes[1]
        if duracion[1]==1: escritura.append(str(duracion[1])+" day")
        else: escritura.append(str(duracion[1])+" days")
    if duracion[4]/constantes[2]>=1:
        duracion[2]=int(duracion[4]/constantes[2])
        duracion[4]=duracion[4]-duracion[2]*constantes[2]
        if duracion[2]==1: escritura.append(str(duracion[2])+" hour")
        else: escritura.append(str(duracion[2])+" hours")
    if duracion[4]/constantes[3]>=1:
        duracion[3]=int(duracion[4]/constantes[3])
        duracion[4]=duracion[4]-duracion[3]*constantes[3]
        if duracion[3]==1: escritura.append(str(duracion[3])+" minute")
        else: escritura.append(str(duracion[3])+" minutes")
    if duracion[4]<constantes[3] and int(duracion[4])!=0:
        if duracion[4]==1: escritura.append(str(duracion[4])+" second")
        else: escritura.append(str(duracion[4])+" seconds")
    #Escritura de la duracion
    if len(escritura)==1:
        return " ".join(escritura)
    else:
        for i in range(len(escritura)):
             
            if i!=len(escritura)-2: escritura[i]+=","
            if i==len(escritura)-1: 
                escritura[i]="and "+ escritura[i]
                escritura[i]=escritura[i].replace(",","")
        return " ".join(escritura)