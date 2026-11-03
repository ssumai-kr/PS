from collections import defaultdict
def solution(gems):
    answer = []

    # 모든 종류의 보석을 1개 이상 포함하는 가장 짧은 구간 찾기
    items = defaultdict(int)
    for g in gems:
        items[g] = items.get(g, 0)

    kinds = len(items)
    count = 0
    n = len(gems)
    i = 0
    best = float('inf')                 # 가장 짧은 길이 (아직 못 찾음 = ∞)

    for j in range(0, n):
        # ① 오른쪽 보석 담기
        items[gems[j]] += 1
        if items[gems[j]] == 1:         # 0 → 1이 됐다면 새 종류가 들어온 거예요
            count += 1

        # ② 모든 종류가 모여 있는 동안 왼쪽 줄이기
        while count == kinds:
            if j - i < best:            # 더 짧으면 갱신 ('<'라서 같은 길이면 앞쪽이 남아요)
                best = j - i
                answer = [i + 1, j + 1] # 진열대 번호는 1부터 시작해요
            items[gems[i]] -= 1         # 왼쪽 보석 빼기
            if items[gems[i]] == 0:     # 1 → 0이 됐다면 그 종류가 사라진 거예요
                count -= 1
            i += 1

    return answer