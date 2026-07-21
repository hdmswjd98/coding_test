def solution(a, b, c):
    answer = 0

    if (len({a,b,c})==3):
        answer = a+b+c
    elif (len({a,b,c}) == 2):
        answer = (a + b + c) * (a**2 + b**2 + c**2 )
    elif (len({a,b,c})==1):
        answer = (a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3 )
    return answer

print(solution(2,6,1))
print(solution(5,3,3))
print(solution(4,4,4))