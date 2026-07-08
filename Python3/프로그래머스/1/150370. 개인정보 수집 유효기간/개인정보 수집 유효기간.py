def solution(today, terms, privacies):
    n = GetDate(today)
    dic, ans = {}, []

    for e in terms:
        tt, ll = e.split()
        dic[tt] = int(ll) * 28

    for i in range(len(privacies)):
        start, plan = privacies[i].split()
        start = GetDate(start)
        plan = dic[plan]

        if n - start >= plan:
            ans.append(i + 1)

    return ans


# 2000년 1월 1일을 기점으로 일수 계산
def GetDate(ss):
    yy, mm, dd = map(int, ss.split("."))
    return (yy - 2000) * 12 * 28 + (mm-1) * 28 + dd