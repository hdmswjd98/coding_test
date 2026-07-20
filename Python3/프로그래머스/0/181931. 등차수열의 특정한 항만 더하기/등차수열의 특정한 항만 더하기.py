def solution(a, d, included):
    answer = 0

# 1항 i=0, included[0], a + (i * d)
# 2항 i=1, included[1], a+(i)*d

    for i in range(len(included)):
        if included[i] == True:
            answer += a + (i * d)

    return answer