import sys
sys.setrecursionlimit(2000)

T, lmap = None, None


class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v


def MakeNode(v, depth, lb, rb):
    global T

    tt = Node(v)

    if depth == len(T) - 1:
        return tt

    lc, rc = None, None

    for e in T[depth + 1]:
        if lb < e < v:
            lc = e

        if v < e < rb:
            rc = e

    if lc is not None:
        tt.left = MakeNode(lc, depth + 1, lb, v)

    if rc is not None:
        tt.right = MakeNode(rc, depth + 1, v, rb)

    return tt


def PreOrder(n, result):
    if n is None:
        return

    result.append(lmap[n.val])
    PreOrder(n.left, result)
    PreOrder(n.right, result)


def PostOrder(n, result):
    if n is None:
        return

    PostOrder(n.left, result)
    PostOrder(n.right, result)
    result.append(lmap[n.val])


def solution(arr):
    global T, lmap

    # 서로 다른 y좌표를 높은 순서의 레벨로 변환
    yy = set()

    for e in arr:
        yy.add(e[1])

    yy = list(yy)
    yy.sort()

    dic = {}

    for i, y in enumerate(yy):
        dic[y] = len(yy) - i - 1

    # 레벨별 x좌표 저장
    T = []

    for _ in range(len(yy)):
        T.append([])

    # x좌표 → 노드 번호
    lmap = {}

    for i, e in enumerate(arr):
        x, y = e
        level = dic[y]

        T[level].append(x)
        lmap[x] = i + 1

    for level in T:
        level.sort()

    tree = MakeNode(T[0][0], 0, -1, 100001)

    preorder_result = []
    postorder_result = []

    PreOrder(tree, preorder_result)
    PostOrder(tree, postorder_result)

    return [preorder_result, postorder_result]