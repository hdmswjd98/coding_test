def solution(nums):
    answer = []
    
    for e in nums:
        answer.append(e*2)
        
    return answer

print(solution([1, 2, 3, 4, 5]))