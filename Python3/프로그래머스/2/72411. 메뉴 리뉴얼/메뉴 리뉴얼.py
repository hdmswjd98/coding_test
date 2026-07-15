N, K, A, dic, ans = None, None, None, None, None

def Eval(A):
    t = list(map(str, A[:K]))
    kk = ''.join(t)
    dic[kk] = dic.get(kk, 0) + 1


def combi(n, f, ss):
    global A, N, K

    if (n == K):
        Eval(A)
        return

    for i in range(f, N):
        A[n] = ss[i]
        combi(n + 1, i + 1, ss)


def Proc(k, orders):
    global N, K, A, dic, ans

    # k요리 course
    # 주문이 BA로 들어올 수 있어서 AB로 통일
    for i in range(len(orders)):
        orders[i] = list(orders[i])
        orders[i].sort()

    K = k
    dic = {}

    for e in orders:
        N = len(e)
        A = [None] * N
        combi(0, 0, e)

    # 여기 각 조합의 출현 회수
    # 랭킹 정하기
    aa = []

    for k in dic:
        # (출현수, key)
        aa.append([-dic[k], k])

    aa.sort()

    if (len(aa) == 0):
        return

    # 조합 미출현
    if (aa[0][0] == -1):
        return 0

    # 최대와 같은 빈도의 조합만 추가
    for e in aa:
        if (e[0] != aa[0][0]):
            return
        else:
            ans.append(e[1])


def solution(orders, tar):
    global ans

    ans = []

    for e in tar:
        Proc(e, orders)

    ans.sort()
    return ans


print(solution(
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    [2, 3, 4]
))