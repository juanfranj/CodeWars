def pick_peaks(arr):
    dic = {'pos':[], 'peaks':[]}
    subiendo = False
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:# and arr[i+1] > arr[i+2]:
            subiendo = True
            pos = i+1
        if subiendo and arr[i] > arr[i+1]:
            dic['pos'].append(pos)
            dic['peaks'].append(arr[pos])
            subiendo = False
            #print("pos: ", i+1)
            #print("peaks: ", arr[i+1])
    return dic

if __name__ == '__main__':
    arr = [2,1,3,2,2,2,2,5,6]
    print(pick_peaks(arr))

'''
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
'''