def Check(str1, str2):
    ll = min(len(str1), len(str2))

    for i in range(ll):
        if str1[i] != str2[i]:
            return i

    return ll


def solution(m):
    m.sort()

    ans = 0
    n = len(m)

    for i in range(n):
        d1 = 0
        d2 = 0

        if i - 1 >= 0:
            d1 = Check(m[i], m[i - 1])

        if i + 1 < n:
            d2 = Check(m[i], m[i + 1])

        mm = max(d1, d2)

        if len(m[i]) == mm:
            ans += mm
        else:
            ans += mm + 1

    return ans