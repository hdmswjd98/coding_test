def solution(id_list, report, k):
    ss = set(report)
    dd, banned = {}, set()

    for r in ss:
        n1, n2 = r.split()
        dd[n2] = dd.get(n2, 0) + 1

    for e in dd:
        if dd[e] >= k:
            banned.add(e)

    ids, R = {}, [0] * len(id_list)

    for i, e in enumerate(id_list):
        ids[e] = i

    for e in ss:
        n1, n2 = e.split()
        if n2 in banned:
            R[ids[n1]] += 1

    return R