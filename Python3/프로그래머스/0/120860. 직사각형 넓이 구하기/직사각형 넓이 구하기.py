def solution(dots):
    if (dots[0][0] == dots[1][0]):
        h = abs(dots[0][1] - dots[1][1])
    if (dots[0][1] == dots[1][1]):
        v = abs(dots[0][0] - dots[1][0])
    if (dots[0][0] == dots[2][0]):
        h = abs(dots[0][1] - dots[2][1])
    if (dots[0][1] == dots[2][1]):
        v = abs(dots[0][0] - dots[2][0])
    if (dots[0][0] == dots[3][0]):
        h = abs(dots[0][1] - dots[3][1])
    if (dots[0][1] == dots[3][1]):
        v = abs(dots[0][0] - dots[3][0])

    return h*v