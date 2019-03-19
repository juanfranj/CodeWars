def bowling_score(frames):
    frames=[i for i in frames if i!=" "]
    puntos=[i for i in frames if i!=" "]
    total=[i for i in frames if i!=" "]
    for i in range(len(frames)):
        if frames[i]=="X": puntos[i]="10"
        if frames[i]=="/": puntos[i]=str(10-int(puntos[i-1]))
    for i in range(len(frames)):
        if frames[i]=="X" and i<len(frames)-2: total[i]=str(int(puntos[i])+int(puntos[i+1])+int(puntos[i+2]))
        if frames[i]=="/": total[i]=str(int(puntos[i])+int(puntos[i+1]))
        if frames[i]=="X" and i>=len(frames)-2: total[i]=puntos[i]
    suma=0
    if frames[-2]=="X":
        for i in range(len(frames)-2): suma+=int(total[i])
    elif frames[-2]=="/":
        for i in range(len(frames)-1): suma+=int(total[i])
    else: 
        for i in range(len(frames)): suma+=int(total[i])
    return suma