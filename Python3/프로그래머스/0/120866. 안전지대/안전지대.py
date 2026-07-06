M, N = None, None
def Valid(r,c):
    if ((r<0) or (r>=M)):
        return False
    if((c<0) or (c>=N)):
        return False
    return True


def solution(board):
    global M,N
    dir = [[0,1],[0,-1],[1,0],[-1,0],
           [1,-1],[1,1],[-1,1],[-1,-1]]
    M,N = len(board), len(board[0])
    for r in range(M):
        for c in range(N):
            if (board[r][c] == 1):
                for e in dir:
                    nr, nc = r+e[0], c+e[1]
                    if ((Valid(nr,nc) == True) and (board[nr][nc] == 0)):
                        board[nr][nc] = 2
    ans = 0
    for r in range(M):
        ans += board[r].count(0)
    return ans

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))