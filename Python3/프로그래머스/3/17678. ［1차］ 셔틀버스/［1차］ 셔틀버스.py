def TimeStamp(t):
    hh = int(t[:2])
    mm = int(t[3:])
    return hh * 60 + mm


def StrTime(ts):
    hh = ts // 60
    mm = ts % 60
    return f"{hh:02d}:{mm:02d}"


def solution(n, t, m, timetable):
    tt = []
    base = TimeStamp("09:00")

    for e in timetable:
        tt.append(TimeStamp(e))

    tt.sort()

    cur = base
    idx = 0
    L = len(tt)

    for i in range(n):
        onbus = 0

        while (
            idx < L
            and onbus < m
            and cur >= tt[idx]
        ):
            idx += 1
            onbus += 1

        cur += t

    # 마지막 버스가 꽉 찬 경우
    if onbus == m:
        return StrTime(tt[idx - 1] - 1)

    # 마지막 버스에 자리가 남은 경우
    else:
        return StrTime(base + (n - 1) * t)