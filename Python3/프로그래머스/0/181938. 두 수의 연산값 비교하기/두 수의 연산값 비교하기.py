def solution(a, b):
    answer = 0
    
    n1 = int(str(a) + str(b))
    n2 = 2 * a * b
    
    if (n1>=n2):
        answer = n1
        
    else: 
        answer = n2
    return answer