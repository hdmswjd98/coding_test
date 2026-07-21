def solution(num_list):
    answer = 0
    mul = 1
    total = 0

    for e in num_list:
        mul *= e
        total += e
    
    if (mul < total **2):
        answer = 1
    elif (mul > total **2):
        answer = 0
    return answer

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))