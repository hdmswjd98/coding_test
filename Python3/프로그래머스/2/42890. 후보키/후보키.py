# 비트와이즈 오어링?  비트와이즈앤드

def Attributes(n, rr):
    a = []
    cnt = 0

    # 이진수 변환
    while n > 0:
        a.append(n % 2)
        cnt += n % 2
        n = n // 2

    ss = set([])

    # 선택된 속성만 이어 붙여 문자열 생성
    for e in rr:
        k = ""

        for i in range(len(a)):
            if a[i] == 1:
                k += e[i]

        ss.add(k)

    # 모든 튜플이 서로 구별되는지 확인
    if len(rr) == len(ss):
        return True

    return False


def solution(relation):
    N = len(relation[0])
    A = 2 ** N

    ss = set([])

    # 모든 속성 조합 탐색
    for n in range(1, A):
        if Attributes(n, relation):

            for e in ss:
                ne = n & e

                if ne == n:
                    ss.remove(e)

                elif ne == e:
                    n = e

            ss.add(n)

    return len(ss)