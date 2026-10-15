def solution(elements):
    n = len(elements)
    ext = elements + elements                # 원형 → 두 번 이어 붙이기
    P = [0] * (2 * n + 1)
    for i, x in enumerate(ext):              # 누적합
        P[i + 1] = P[i] + x
    sums = set()                             # 중복 제거
    for length in range(1, n + 1):           # 길이 1 ~ n
        for start in range(n):               # 시작 위치 0 ~ n-1
            sums.add(P[start + length] - P[start])
    return len(sums)