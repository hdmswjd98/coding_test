def tonum(s):
    ss =0
    for e in s:
        ss = ss*2 + int(e)
    return ss


def solution(b1, b2):
    b1 = tonum(b1)
    b2 = tonum(b2)
    
    ans = b1+b2

    
    if ans == 0:
        return "0"
    
    aa = []
    while (ans>0):
        aa.append(ans %2)
        ans = ans // 2 # 2진수 변환? 
        
    aa.reverse()
    aa = list(map(str,aa))
    
    return ''.join(aa)