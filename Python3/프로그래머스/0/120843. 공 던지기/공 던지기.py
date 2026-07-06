def solution(A, k):
    if(len(A) %2 != 0):
        A.extend(A)
    k = 2*(k-1)
    k = k% len(A)
    return A[k]