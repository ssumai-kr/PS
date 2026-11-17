from itertools import combinations
T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    best = 0
    for r in range(1, N + 1):                 # 재료 1개 ~ N개 고르기
        for combo in combinations(items, r):
            cal = sum(k for _, k in combo)
            if cal <= L:
                best = max(best, sum(t for t, _ in combo))

    print(f"#{tc} {best}")