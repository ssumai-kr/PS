def to_base(n, k):
    s = ""
    while n:
        s = str(n % k) + s
        n //= k
    return s or "0"

def solution(s):
    turns = 0
    deleted = 0

    while s != "1":
        base = s.count("0")          # 이번에 지울 0의 개수
        temp = ""
        for ch in s:
            if ch == "0":
                continue
            temp += ch                # 0 빼고 이어 붙이기
        s = to_base(len(temp), 2)     # 길이 → 2진수
        turns += 1
        deleted += base

    return [turns, deleted]