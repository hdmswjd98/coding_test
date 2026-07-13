def solution(arr):
    ans = []
    
    for e in arr:
        if len(ans)==0:
            ans.append(e)

        if(ans[-1] != e):
            ans.append(e)
    return ans