def dirReduc(arr):
    if len(arr)==0: return []
    situacion=[arr[0]]
    for i in range(1,len(arr)):
        if len(situacion)==0: situacion.append(arr[i])
        else:
            if arr[i]=="NORTH":
                if situacion[-1]=="SOUTH" and len(situacion)>0: situacion.pop()
                else: situacion.append(arr[i])
            elif arr[i]=="SOUTH":
                if situacion[-1]=="NORTH" and len(situacion)>0: situacion.pop()
                else: situacion.append(arr[i])
            elif arr[i]=="EAST":
                if situacion[-1]=="WEST" and len(situacion)>0: situacion.pop()
                else: situacion.append(arr[i])
            elif arr[i]=="WEST":
                if situacion[-1]=="EAST" and len(situacion)>0: situacion.pop()
                else: situacion.append(arr[i])
    return situacion