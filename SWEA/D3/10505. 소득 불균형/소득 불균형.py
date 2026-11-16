
T = int(input())

for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    avg = sum(L)/len(L)
    count = 0
    for l in L:
        if l <= avg:
            count += 1

    print(f"#{i+1} {count}")