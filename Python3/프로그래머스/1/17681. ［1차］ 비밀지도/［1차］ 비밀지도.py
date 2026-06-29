def solution(n,arr1, arr2):
    ss = " #"
    a = []

    for i in range(n):
        t = arr1[i] | arr2[i]
        r = []

        for j in range(n):
            r.append(ss[t%2])
            t = t//2
        r.reverse()
        a.append(''.join(r))

    return a

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))