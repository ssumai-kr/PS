from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)          # 합은 처음에 한 번만 계산

    if (s1 + s2) % 2 == 1:             # 홀수면 불가능
        return -1

    limit = len(q1) * 3                # 무한 반복 방지 상한
    count = 0
    while count <= limit:
        if s1 == s2:
            return count
        if s1 > s2:                    # 큰 쪽에서 빼서 작은 쪽에 넣기
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            s2 -= x
            s1 += x
        count += 1
    return -1