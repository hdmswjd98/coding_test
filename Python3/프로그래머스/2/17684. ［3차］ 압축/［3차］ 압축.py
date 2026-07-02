def solution(msg):
    dic, c ={}, ord('A') 
    for i in range(26):
        kk = ""+chr(c+i)
        dic[kk] = i+1   

# anc는 검사할 스트링의 첫 위치
    anc, idx, n = 0, 27, len(msg)
    ans, i = [], 1
    while (i <=n):
        k = msg[anc:i]
        if ((k in dic) == True):
            e, i = dic[k], i+1
        else:
            ans.append(e)
            dic[k], idx = idx, idx+1
            anc = i-1
            i = anc +1  
    ans.append(e)
    return ans

###while문 안에를 직접 짜보기 