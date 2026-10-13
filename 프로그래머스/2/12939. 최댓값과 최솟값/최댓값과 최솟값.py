def solution(s):
    answer = ''
    
    nums = list(map(int, (s.split())))
    
    maxn, minn = max(nums), min(nums)
    
    answer += str(minn) + " "
    answer += str(maxn)
    
    
    
    return answer