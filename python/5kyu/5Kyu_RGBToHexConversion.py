def rgb(r, g, b):
    col = [r, g, b]
    aux = []
    for i in col:
        if i > 255:
            aux.append(255)
        elif i < 0:
            aux.append(0)
        else:
            aux.append(i)

    return f"{aux[0]:02X}{aux[1]:02X}{aux[2]:02X}"

if __name__ == '__main__':
    r = 254
    g = 253
    b = 252
    print(rgb(r, g, b))

'''
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
'''