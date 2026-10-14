def solution(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:   # 맨 위 글자와 같으면 짝 → 제거
            stack.pop()
        else:
            stack.append(ch)            # 다르면 쌓기
    return 1 if not stack else 0        # 다 지워졌으면 1