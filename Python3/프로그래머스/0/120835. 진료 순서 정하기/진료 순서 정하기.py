# A = [3,0], [76,1], [24,2]
# A = [76,1], [24,2], [3,0]

def solution(em):
    n = len(em)
    answer = [-1]*n
    A = []

    for i,e in enumerate(em):
        A.append([-e,i])
    A.sort()
    idx = 1
    
    for e in A:
        answer[e[1]] = idx
        idx += 1
    return answer