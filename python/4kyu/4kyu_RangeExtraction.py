def solution(args):
    text = ''
    tam = len(args)
    for i in range(tam):
        if i != 0 and i!= tam-1:
            if (args[i] - args[i-1]) != 1:
                text += str(args[i]) + ','
            else:
                if (args[i+1] - args[i]) == 1:
                    text = text[:-1] +'-'
                else:
                    text += str(args[i]) + ','
        else:
            if i == 0:
                text += str(args[i]) + ','
            else:
                text += str(args[i])
        
    return text

if __name__  == '__main__':
   arr = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20] #Sol: '-6,-3-1,3-5,7-11,14,15,17-20'
   sol = solution(arr)
   print(sol)

'''
    Best Solution
    
    def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)
    '''
