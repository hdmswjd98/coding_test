def solution(arr, delete):
    answer = []
    
    for e in arr :
        if e not in delete :
            answer.append(e)
    return answer