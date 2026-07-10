def solution(my, str, s):
    answer = ''  

    a = len(str) + s

    answer = my[:s] + str + my[a:]

    return answer


print(solution("He11oWor1d",	"lloWorl"	,2))