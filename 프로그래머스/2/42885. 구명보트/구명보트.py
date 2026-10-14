def solution(people, limit):
    people.sort()                        # 가벼운 순으로 정렬
    i, j = 0, len(people) - 1            # i = 가장 가벼운, j = 가장 무거운
    boats = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1                       # 가벼운 사람도 같이 탐
        j -= 1                           # 무거운 사람은 무조건 탐
        boats += 1                       # 보트 하나 사용
    return boats