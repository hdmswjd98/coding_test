def solution(friends, gifts):
    n = len(friends)

    A = []
    G = [0] * n
    X = [0] * n

    for i in range(n):
        A.append([0] * n)

    answer = 0
    dic = {}

    # 이름 -> 인덱스 매핑
    for i in range(n):
        dic[friends[i]] = i

    # 선물 기록 저장
    for e in gifts:
        n1, n2 = e.split()
        n1, n2 = dic[n1], dic[n2]

        A[n1][n2] += 1
        X[n1] += 1
        X[n2] -= 1

    # 두 사람씩 비교
    for i in range(n):
        for j in range(i + 1, n):
            win = -1

            if A[i][j] > A[j][i]:
                win = i

            elif A[i][j] < A[j][i]:
                win = j

            else:
                if X[i] > X[j]:
                    win = i
                elif X[i] < X[j]:
                    win = j

            # 승자가 있으면 다음 달 선물 1개 받음
            if win != -1:
                G[win] += 1

    return max(G)