def solution(board, skill):
    n, m = len(board), len(board[0])
    D = [[0] * (m + 1) for _ in range(n + 1)]      # 끝+1 칸까지 쓰니까 한 칸 크게

    # 1) 네 귀퉁이 표시
    for t, r1, c1, r2, c2, degree in skill:
        v = -degree if t == 1 else degree
        D[r1][c1] += v
        D[r1][c2+1] -= v
        D[r2+1][c1] -= v
        D[r2+1][c2+1] += v

    # 2) 가로로 누적
    for i in range(n):
        for j in range(1, m):
            D[i][j] += D[i][j-1]
    # 3) 세로로 누적
    for j in range(m):
        for i in range(1, n):
            D[i][j] += D[i-1][j]

    # 4) 살아 있는 건물 세기
    return sum(1 for i in range(n) for j in range(m) if board[i][j] + D[i][j] > 0)