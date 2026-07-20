def solution(code):
    ret=''
    mode = 0

    for idx in range(len(code)):

        if (mode==0) and (code[idx] != "1") and (idx % 2 == 0):
            ret += code[idx]
            # print(code[idx])
        elif (mode==0) and (code[idx] == "1"):
            mode = 1

        elif (mode==1) and (code[idx] != "1") and (idx % 2 == 1):
            ret += code[idx]
            # print(code[idx])
        elif (mode==1) and (code[idx]=="1"):
            mode = 0

    if ret == '':
        ret = "EMPTY"

    return ret

print(solution("abc1abc1abc"))