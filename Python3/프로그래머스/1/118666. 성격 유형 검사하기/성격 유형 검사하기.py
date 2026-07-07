def solution(s,ch):
    M,dic,L = "RTCFJMAN",{}, len(s)
    for e in M:
        dic[e] = 0
    for i in range(L):
        ss = ch[i] - 4
        if (ss<0):
            dic[s[i][0]] -= ss
        else:
            dic[s[i][1]] += ss
    answer = ""

    for i in range(0,8,2):
        t1, t2 = dic[M[i]], dic[M[i+1]]
        if (t1<t2):
            answer += M[i+1]
        elif (t1>t2):
            answer += M[i]
        else:
            answer += min(M[i], M[i+1])
    return answer