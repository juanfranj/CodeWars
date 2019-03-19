def isValidWalk(walk):
    origen=[0,0]
    for i in walk:
        if len(walk)==10:
            if i=="e":
                origen[1]+=1
            elif i=="w":
                origen[1]+=-1
            elif i=="n":
                origen[0]+=1
            elif i=="s":
                origen[0]+=-1
        else:
            return False
    if origen[0]==0 and origen[1]==0:
        return True
    else:
        return False