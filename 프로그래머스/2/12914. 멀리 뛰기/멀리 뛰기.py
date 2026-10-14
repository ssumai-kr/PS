def solution(n):
    answer = 0
    
    # 한칸 아님 두칸이다.
    dp = [0] * (n+2) # n=1일때, dp[2]도 쓸 수 있도록
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    
    answer = dp[n]
    
    return answer