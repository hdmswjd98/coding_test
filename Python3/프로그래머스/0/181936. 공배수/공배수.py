def solution(num, n, m):
    answer = 0
    
    if ((num%n==0) and (num%m==0)):
        answer = 1
    else:
        answer = 0
    return answer

print(solution(60,2,3))
print(solution(55,10,5))