def solution(a, b):
    answer = 0
    
    n1 = str(a)+str(b)
    n2 = str(b)+str(a)
    
    if (n1>=n2):
        answer = int(n1)
    else:
        answer = int(n2)
    
    return answer