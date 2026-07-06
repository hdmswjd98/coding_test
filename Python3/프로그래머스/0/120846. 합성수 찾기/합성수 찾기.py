def IsPrime(n):
    i = 2
    while(i*i<=n):
        if(n%i == 0):
            return False
        i = i+1
    return True

def solution(n):
    cnt = 0
    for i in range(2,n+1):
        if(IsPrime(i) == False):
            cnt = cnt + 1
    return cnt