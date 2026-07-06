def solution(ll):
    ll = list(ll.split())
    A = []
    for e in ll :
        if (e == 'Z'):
            A.pop()
        else:
            A.append(int(e))
    return sum(A)
