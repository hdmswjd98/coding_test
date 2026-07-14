def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        if a % b == 0:
            return b
        a, b = b, a % b

    return 1


def Check(sig, n):
    for e in sig:
        nn = n % sum(e)

        # 노란불 구간인지 확인
        if (nn >= e[0]) and (nn < e[0] + e[1]):
            continue
        else:
            return False

    return True


def solution(sig):
    N = len(sig)
    ll = []

    # 각 신호등의 전체 주기 저장
    for e in sig:
        ll.append(sum(e))

    # 전체 주기(최소공배수) 계산
    g = ll[0]

    for e in ll:
        g = gcd(g, e)

    v = g

    for e in ll:
        v = v * e // g

    # 전체 주기 동안 탐색
    for i in range(v):
        if Check(sig, i):
            return i + 1

    return -1