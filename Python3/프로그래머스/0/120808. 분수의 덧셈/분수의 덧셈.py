import math

def solution(n1, d1, n2, d2):
    d = d1 * d2
    n = (n1*d2) + (n2*d1)
    
    g = math.gcd(d,n)
    
    
    answer = [n//g, d//g]
    
    
    return answer