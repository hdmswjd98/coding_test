def solution(arr,q):
    l,r,L = 0, len(arr)-1, len(arr)
    for i in range(len(q)):
        if(i%2 == 0):
            dd = L -q[i] -1
            r,L = r-dd, L-dd
        else:
            dd = q[i]
            l,L = l+dd, L-dd
        # print(arr[l:r+1])
    return arr[l:r+1]