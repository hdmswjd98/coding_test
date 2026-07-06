def distance(n1, n2):  # 순서: 행과 열
    return abs(n1 // 3 - n2 // 3) + abs(n1 % 3 - n2 % 3)


def solution(numbers, hand):
    keys, dic = "123456789*0#", {}

    # 순서번호
    for i, e in enumerate(keys):
        dic[e] = i

    l, r = dic['*'], dic['#']  # 초기 위치
    move = []

    for k in numbers:
        e = dic[str(k)]
        m = None

        if e % 3 == 0:  # 왼쪽
            m, l = 'L', e

        elif e % 3 == 2:  # 오른쪽
            m, r = 'R', e

        else:
            # 현재 각 손의 위치 추적
            # 키의 행과 열 위치
            # 거리 계산
            d1 = distance(e, l)
            d2 = distance(e, r)

            if d1 < d2:
                m, l = 'L', e

            elif d1 > d2:
                m, r = 'R', e

            else:  # 거리도 같으면
                if hand == 'left':
                    m, l = 'L', e
                else:
                    m, r = 'R', e

        move.append(m)

    return ''.join(move)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	,"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	,"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	,"right"))