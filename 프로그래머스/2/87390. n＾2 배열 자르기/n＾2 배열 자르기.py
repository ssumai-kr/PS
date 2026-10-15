def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):       # 필요한 칸만
        r, c = divmod(idx, n)                 # 1차원 위치 → (행, 열)
        answer.append(max(r, c) + 1)          # 작성한 규칙과 같은 값
    return answer