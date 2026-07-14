def solution(bb, moves):
    answer = 0
    stack, board = [], []

    M, N = len(bb), len(bb[0])

    # 컬럼 수에 해당하는 스택을 만듦
    for i in range(N):
        board.append([])

    for c in range(N):
        for r in range(M):
            if (bb[r][c] == 0):
                continue
            board[c].append(bb[r][c])

    for e in board:
        e.reverse()

    # 명령대로 인형을 뽑음
    for c in moves:
        c = c - 1

        if (len(board[c]) == 0):
            continue

        doll = board[c].pop()

        # 뽑기 스택으로 이동하면서 제거 여부 판단
        if ((len(stack) > 0) and (stack[-1] == doll)):
            answer += 2
            stack.pop()
        else:
            stack.append(doll)

    return answer