def solution(sequence, k):
    n = len(sequence)
    p = [0] * (n + 1)
    for i, s in enumerate(sequence):
        p[i+1] = p[i] + sequence[i]

    answer = []
    minlen = float('inf')          # ④
    i = 0                          # ①
    for j in range(n):             # j는 끝(오른쪽)을 한 칸씩 늘림
        while p[j+1] - p[i] > k:   # ② 합이 넘치면 i를 당김
            i += 1
        if p[j+1] - p[i] == k and j - i < minlen:
            minlen = j - i
            answer = [i, j]        # ⑤
    return answer