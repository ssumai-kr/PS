from collections import Counter

def solution(participant, completion):
    answer = ''
    
    #완주하지 못한 선수의 이름을 return 하라
    #즉 참가자에서 완주자를 비교하면됨
    
    ans = Counter(participant) - Counter(completion)
    
    answer = ans.most_common()[0][0]
    
    
    return answer