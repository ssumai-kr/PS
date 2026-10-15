def solution(nums):
    answer = 0
    n = len(nums)
    #총 N마리 중 N/2마리를 가져가도 좋다
    pokemons = set(nums)
    
    if len(pokemons) <= n // 2:
        answer = len(pokemons)
    else:
        answer = n//2
    
    return answer