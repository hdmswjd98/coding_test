def IsPrime(n):
    i = 2
    while(i*i<=n):
        if(n%i == 0):
            return False
        i = i+1
    return True

def solution(n):
    A = []
    for i in range(2,n+1):
        if(IsPrime(i) == True):
            if(n%i==0):
                A.append(i)
    return(A)

print(solution(12))
print(solution(17))
print(solution(420))