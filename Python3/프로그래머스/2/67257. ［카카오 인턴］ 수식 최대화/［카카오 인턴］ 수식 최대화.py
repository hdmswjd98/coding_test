ops = ['+', '-', '*']


def Eval():
    global A, mm

    post = PostFix(A)
    ans = Calc(post)

    mm = max(mm, abs(ans))


def perm(n):
    global A, V

    if n == 3:
        Eval()
        return

    for i in range(3):
        if V[i] == False:
            V[i] = True
            A[n] = i

            perm(n + 1)

            V[i] = False


def PostFix(pr):
    global expr

    st = []
    res = []
    dic = {}

    for i in range(3):
        dic[ops[i]] = pr[i]

    for e in expr:
        if e not in ops:
            res.append(e)
            continue

        while len(st) > 0 and dic[st[-1]] >= dic[e]:
            res.append(st.pop())

        st.append(e)

    while len(st) != 0:
        res.append(st.pop())

    return res


def Calc(post):
    st = []

    for e in post:
        if e not in ops:
            st.append(int(e))

        else:
            n2 = st.pop()
            n1 = st.pop()

            if e == '+':
                st.append(n1 + n2)

            elif e == '-':
                st.append(n1 - n2)

            else:
                st.append(n1 * n2)

    return st[0]


def solution(ex):
    global expr, A, V, mm

    A = [-1] * 3
    V = [False] * 3
    mm = 0

    expr = ex.replace('+', ' + ')
    expr = expr.replace('-', ' - ')
    expr = expr.replace('*', ' * ')

    expr = list(expr.split())

    perm(0)

    return mm


print(solution("100-200*300-500+20"))