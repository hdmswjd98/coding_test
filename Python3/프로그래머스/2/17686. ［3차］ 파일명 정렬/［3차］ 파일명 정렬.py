def IsDigit(cc):
    if ((cc >='0') and (cc<='9')):
        return True
    else:
        return False

def solution(files):
    A, idx =[], 0
    for e in files:
        tt, j = [e], 0
        e = e.lower()
        while (IsDigit(e[j])== False):
            j +=1
        tt.append(e[:j])
        anc = j
        while ((j<len(e)) and (IsDigit(e[j])== True)):
            j +=1
        tt.append(int(e[anc:j]))
        tt.append(e[j:])
        tt.append(idx)
        A.append(tt)
        idx +=1

    #for e in A:
    # print(e)
    A.sort(key=lambda x:x[4])
    A.sort(key=lambda x:x[2])
    A.sort(key=lambda x:x[1])
    ans =[]
    for e in A:
        ans.append(e[0])

    return ans