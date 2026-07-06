def IsDigit(c):
    if (ord(c) < ord('0')):
        return False
    if (ord(c) > ord('9')):
        return False
    return True

def solution(my_string):
    a = []
    for e in my_string:
        if(IsDigit(e) == True):
            a.append(e)
        else:
            a.append(' ')
    a = ''.join(a)
    a = list(map(int, a.split()))
    return sum(a)