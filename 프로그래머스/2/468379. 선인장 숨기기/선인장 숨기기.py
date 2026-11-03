from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1                     # 끝까지 비가 안 오는 칸
    T = [[INF] * n for _ in range(m)]
    for t, (r, c) in enumerate(drops, 1):
        T[r][c] = t                          # 이 칸이 젖는 시각

    # 1단계: 가로로 w칸씩 최솟값  → R[i][j] = min(T[i][j .. j+w-1])
    R = []
    for i in range(m):
        row = T[i]
        dq = deque()                         # 인덱스 저장, 값은 오름차순 유지
        res = []
        for j in range(n):
            while dq and row[dq[-1]] >= row[j]:
                dq.pop()
            dq.append(j)
            if dq[0] <= j - w:               # 창 밖으로 나간 앞쪽 제거
                dq.popleft()
            if j >= w - 1:
                res.append(row[dq[0]])
        R.append(res)

    # 2단계: 세로로 h칸씩 최솟값 → W[i][j] = 구역 (i,j)~(i+h-1, j+w-1)의 최솟값
    cols = n - w + 1
    W = [[0] * cols for _ in range(m - h + 1)]
    for j in range(cols):
        dq = deque()
        for i in range(m):
            while dq and R[dq[-1]][j] >= R[i][j]:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - h:
                dq.popleft()
            if i >= h - 1:
                W[i - h + 1][j] = R[dq[0]][j]

    # 3단계: 가장 늦게 젖는 구역 (위 → 왼쪽 순서로 훑으면서 '>'일 때만 갱신)
    best, answer = -1, [0, 0]
    for i in range(m - h + 1):
        for j in range(cols):
            if W[i][j] > best:
                best = W[i][j]
                answer = [i, j]
    return answer