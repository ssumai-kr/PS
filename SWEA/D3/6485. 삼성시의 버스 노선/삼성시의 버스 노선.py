T = int(input())

for i in range(T):
    ans = []
    N = int(input())

    dist = [0] * 5002

    for _ in range(N):
        A, B = map(int, input().split())

        for s in range(A, B+1):
            dist[s] += 1

    P = int(input())

    for _ in range(P):
        C = int(input())

        ans.append(dist[C])
    print(f"#{i+1}", *ans)