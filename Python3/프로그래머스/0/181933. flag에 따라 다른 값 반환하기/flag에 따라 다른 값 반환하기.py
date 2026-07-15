def solution(a, b, flag):
    answer = 0

    if flag:
        answer = a+b
    else:
        answer = a-b
    return answer

print(solution(-4,	7, 1))
print(solution(-4	,7	,0))