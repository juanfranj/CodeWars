def zero(*arg):
    if len(arg)==0: return 0 
    else: return calculo("".join(arg)+"0")
def one(*arg):
    if len(arg)==0: return 1 
    else: return calculo("".join(arg)+"1")
def two(*arg):
    if len(arg)==0: return 2 
    else: return calculo("".join(arg)+"2")
def three(*arg):
    if len(arg)==0: return 3 
    else: return calculo("".join(arg)+"3")
def four(*arg):
    if len(arg)==0: return 4 
    else: return calculo("".join(arg)+"4")
def five(*arg): 
    if len(arg)==0: return 5 
    else: return calculo("".join(arg)+"5")
def six(*arg):
    if len(arg)==0: return 6 
    else: return calculo("".join(arg)+"6")
def seven(*arg):
    if len(arg)==0: return 7 
    else: return calculo("".join(arg)+"7")
def eight(*arg):
    if len(arg)==0: return 8 
    else: return calculo("".join(arg)+"8")
def nine(*arg):
    if len(arg)==0: return 9 
    else: return calculo("".join(arg)+"9")
def plus(arg): return str(arg)+"+"
def minus(arg): return str(arg)+"-"
def times(arg): return str(arg)+"*"
def divided_by(arg): return str(arg)+"/"
def calculo(op):
    op=op[::-1]
    if op[1] == "+": return int(op[0])+int(op[2])
    elif op[1] == "*": return int(op[0])*int(op[2])
    elif op[1] == "-": return int(op[0])-int(op[2])
    elif op[1] == "/": return int(op[0])//int(op[2])