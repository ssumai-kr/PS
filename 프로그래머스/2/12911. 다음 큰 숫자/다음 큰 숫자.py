def to_base(n, k):
    s = ""
    while n:
        s = str (n%k) + s
        n //= k
    return s or "0"

def solution(n):
    
    # n의 다음 큰 숫자는 n 보다 크다
    # 2진수로 변환 했을 때 1의 갯수가 같다
    # 조건 1, 2 를 만족하는 가장 작은 수 이다.
    
    # n <= 1,000,000
    
    oneCount = (to_base(n,2)).count("1")
    next = n
    while True:
        next = next + 1
        if oneCount == (to_base(next,2)).count("1"):
            return next
        