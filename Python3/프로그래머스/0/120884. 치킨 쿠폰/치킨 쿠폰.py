def solution(chicken):
    ss = 0
    while(True):
        ll = chicken // 10
        if (ll==0):
            return ss
        ss += ll
        chicken = chicken % 10 + ll