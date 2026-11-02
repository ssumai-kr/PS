def solution(people, limit):
    answer = 0
    
    #힌번에 최대 2명씩만 탈 수 있고, 무게 제한 있음
    
    people.sort()
    
    i, j = 0, len(people) -1
    
    boats = 0
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    
    answer = boats
    return answer