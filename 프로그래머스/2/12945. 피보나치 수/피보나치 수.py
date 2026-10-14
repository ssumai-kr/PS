def solution(n):
    answer = 0
    
    #이녀석이 dp 의 정석 아니던가?
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    # print(dp)
    
    for i in range(2, n+1):
        # print(i)
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567
    
    answer = dp[n]
    return answer