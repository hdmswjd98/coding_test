T, N, ans, D = None, None, 100000, None

# pruning 조건
# - 이미 최소값을 넘은 경우
# - 하나씩밖에 점검이 안되는데 친구가 얼마 안 남은 경우
def solution(n, weak, dist):
    global T, N, D, ans

    D = dist
    T = n
    N = len(D)

    D.sort(key=lambda x: -x)

    # 점검할 외벽
    ll = []
    for e in weak:
        ll.append(e)

    # 0번 친구부터 점검할 외벽
    dfs(0, ll)

    if (ans == 100000):
        return -1

    return ans

def dfs(n, ll):
    global T, N, D, ans

    # 모든 외벽이 점검됨
    if (len(ll) == 0):
        ans = min(ans, n)
        return

    # 모든 친구 소모 또는 이미 최소를 넘음
    if ((n >= N) or (n > ans)):
        return

    for anc in ll:
        # ll1 : 시계방향으로 갈 때 못 가는 곳
        # ll2 : 반시계방향으로 갈 때 못 가는 곳
        ll1, ll2 = [], []

        for e in ll:
            dd = (e - anc + T) % T

            if (dd > D[n]):
                ll1.append(e)

            dd = T - dd

            if ((dd != T) and (dd > D[n])):
                ll2.append(e)

        s1, s2 = len(ll1), len(ll2)
        ss = min(s1, s2)

        # 하나만 점검
        if (ss + 1 == len(ll)):
            # 남은 친구 수와 외벽의 수 비교
            if (N - n - 1 >= ss):
                ans = min(ans, n + ss + 1)
            continue

        # 거리는 짧아지므로 다음 친구도 오직 하나만
        if (s1 < s2):
            dfs(n + 1, ll1)
        else:
            dfs(n + 1, ll2)