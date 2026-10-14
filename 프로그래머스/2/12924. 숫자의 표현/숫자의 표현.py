def solution(n):
    answer = 0
    
    #자연수 n 을 연속한 자연수들로 표현 하는 방법이 여러가지다
    
    count = 1 # 본인 수
    
    
    for i in range(1, n):
        sum = i
        for j in range(i+1, n):
            sum += j
            if(sum == n):
                count += 1
                break
            elif sum > n:
                break
        
    
    answer = count
    return answer