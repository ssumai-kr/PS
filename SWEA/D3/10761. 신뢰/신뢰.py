T = int(input())
for tc in range(1, T + 1):
    data = input().split()
    N = int(data[0])

    pos = {'O': 1, 'B': 1}    # 현재 위치
    last = {'O': 0, 'B': 0}   # 각 로봇이 마지막으로 버튼을 누른 시각
    time = 0                  # 전체 진행 시각

    for j in range(N):
        who = data[1 + 2 * j]
        p = int(data[2 + 2 * j])
        time = max(last[who] + abs(p - pos[who]), time) + 1 #버튼을 누르는데에도 1초가 걸리니까 +1
        pos[who] = p
        last[who] = time

    print(f"#{tc} {time}")