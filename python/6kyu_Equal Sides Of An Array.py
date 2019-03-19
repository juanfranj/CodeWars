def find_even_index(arr):
    sol=-1
    for i in range(len(arr)):
        if i==0:
            if 0==sum(arr[i+1:]):
                #print(sum(arr[:i]),sum(arr[-i:]),"OK")
                sol=i
                break
        elif i>0 and i<len(arr):
            if sum(arr[:i])==sum(arr[i+1:]):
                #print(sum(arr[:i]),sum(arr[-i:]),"OK")
                sol=i
                break
        elif i==len(arr):
            if sum(arr[:i-1])==0:
                print("ok")
                #print(sum(arr[:i]),sum(arr[-i:]),"OK")
                sol=i
                break
    return sol