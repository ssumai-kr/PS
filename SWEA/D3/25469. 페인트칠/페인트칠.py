T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    #H행 W열

    # #-> 검은색 . -> 흰색

    x = set()
    y = set()

    board = [input().strip() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                x.add(i)
                y.add(j)

    if not x:
        ans = min(H, W)
    else:
        ans = (W - len(x)) + (H- len(y))

    print(ans)