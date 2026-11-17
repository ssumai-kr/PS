T = 10

for tc in range(1, T + 1):
    N = int(input())
    ans = [0] * N
    buildings = list(map(int, input().split()))
    #하나 빌딩 리스트 들어옴

    for j in range(2, N-2):
        left = -1
        right = -1
        if buildings[j-2] < buildings[j] and buildings[j-1] < buildings[j]:
            left = max(buildings[j-2], buildings[j-1])
        if buildings[j+2] < buildings[j] and buildings[j+1] < buildings[j]:
            right = max(buildings[j+2], buildings[j+1])

        if left == -1 or right == -1:
            continue

        ans[j] = buildings[j] - max(left, right)        

    print(f"#{tc} {sum(ans)}")       