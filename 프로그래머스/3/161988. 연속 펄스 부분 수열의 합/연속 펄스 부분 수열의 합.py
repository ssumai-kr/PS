def solution(sequence):
    answer = 0
    
    #펄스 수열이란 1 과 -1이 번갈아 나오는 수열
    # 연속 펄스 부분 수열의 합 중 가장 큰 것을 return
    
    # 부분 구간합 중에서 가장 큰 것을 return
    n = len(sequence)
    plusS = [0] * n
    minusS = [0] * n
    
    plusD = [0] * (n + 1)
    minusD = [0] * (n + 1)
    
    
    
    plus = 1
    minus = -1
    
    for i, s in enumerate(sequence):
        plusS[i] = sequence[i] * (plus * -1)
        plus *= -1
        
        minusS[i] = sequence[i] * (minus * -1)
        minus *= -1
        
    # 구간합 구하기
    
    for i, s in enumerate(sequence):
        plusD[i+1] = plusD[i] + plusS[i]
        minusD[i+1] = minusD[i] + minusS[i]
        
    for D in (plusD, minusD):
        min_left = D[0]
        for r in range(1, n + 1):
            answer = max(answer, D[r] - min_left)
            min_left = min(min_left, D[r])   
    
        
#     print(plusS)
#     print(minusS)
    
#     print(plusD)
#     print(minusD)
        
        
    
    
    return answer