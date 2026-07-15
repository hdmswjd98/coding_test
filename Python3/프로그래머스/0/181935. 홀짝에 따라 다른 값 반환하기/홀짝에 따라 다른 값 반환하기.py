def solution(n):
    answer = 0

    if(n%2!=0): #홀수
        for i in range(1,n+1,2):
            answer += i
            # print(i)

    else: #짝수
        for i in range(2,n+1,2):
                answer += i**2
                # print(i)

    return answer

print(solution(7))
print()
print(solution(10))