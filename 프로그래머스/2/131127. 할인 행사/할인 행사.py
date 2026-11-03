from collections import defaultdict, Counter, deque

def solution(want, number, discount):  # 할인 행사: 크기 10 고정 창
    need = dict(zip(want, number))
    win = Counter(discount[:10])
    ans = 1 if all(win[w] == c for w, c in need.items()) else 0
    for i in range(10, len(discount)): # 10번째 부터 들어오고, 0번 부터 나간다
        win[discount[i]] += 1               # 오른쪽 하나 들어오고
        win[discount[i - 10]] -= 1          # 왼쪽 하나 나가고
        if all(win[w] == c for w, c in need.items()):
            ans += 1
    return ans