from math import gcd #최대 공약수

def solution(arr):
    answer = arr[0]
    
    for x in arr[1:]:
        #최소공배수 = LCM(a,b) = a * b // gcd(a, b)
        answer = answer * x // gcd(answer, x)
    
    
    
    return answer