from functools import cmp_to_key

def comp(a, b):
    n1 = a[0] * b[1]
    n2 = a[1] * b[0]
    return n1-n2


def solution(N, stages):
    stat = []

    for i in range(N + 1):
        stat.append([0, 0, i + 1])

    for ee in stages:
        e = ee - 1

        for i in range(e + 1):
            stat[i][0] += 1

        stat[e][1] += 1

    # 3이라면 1,2,3 스테이지까지 도달
    # 3에서 실패한 상태
    # Stat[분모, 분자, stage]

    stat.pop()

    # 분모가 0인 거 처리, 분자를 0으로
    for i in range(len(stat)):
        if stat[i][0] + stat[i][1] == 0:
            stat[i][0] = 1

    # 분수 비교일 때 컴퓨터의 소수 손실 문제
    # 정수로 비교하는 게 안전
    # a1/a0 vs. b1/b0 → a1*b0 vs. a0*b1
    # 내림차순 vs. 오름차순

    stat.sort(key=lambda x: x[2])
    stat = sorted(stat, key=cmp_to_key(comp))

    ans = []

    for e in stat:
        ans.append(e[2])

    return ans