def solution(A, B):
    A.sort()                    # 오름차순
    B.sort(reverse=True)        # 내림차순
    return sum(a * b for a, b in zip(A, B))