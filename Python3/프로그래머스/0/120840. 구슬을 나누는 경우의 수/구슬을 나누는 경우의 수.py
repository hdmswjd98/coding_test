def solution(n,k):
    k = min(k, n-k) # 6C2 = 6C4니까.. 
    n1, n2 = 1, 1
    for i in range(k):
        n1 = n1 * (n-i)
        n2 = n2 *(i+1)
    return n1//n2


