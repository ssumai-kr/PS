

# def solution(genres, plays):
#     answer = []
#     # 1. 노래가 가장 많이 재생된 장르 먼저 수록
#     # 2. 장르 내에서 많이 재생된 노래 먼저 수록
#     # 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유번호가 낮은 노래가 먼저
#     # 재생된 장르 -> 장르 내 재생 횟수
    
#     #베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 retuern 되도록
    
#     # 고유 번호 = i 인덱스
    
#     playcount = {}

#     for i, count in enumerate(plays):
#         playcount[i] = count
        
#     #print(sorted(playcount, key = lambda x : -playcount[x]))
    
#     k = list(sorted(playcount, key = lambda x : -playcount[x]))
#     print(k)
    
#     mostgenere = genres[sorted(playcount, key = lambda x : -playcount[x])[0]]
    
# #     sortedgenere = [a for a in sorted(playcount, key = lambda x : -playcount[x])]
    
# #     print(sortedgenere)

#     sortedgenere = []
#     for i in k:
#         if genres[i] in sortedgenere:
#             continue
#         else:
#             sortedgenere.append(genres[i])
            
#     #print(sortedgenere)
    

#     return answer


def solution(genres, plays):
    answer = []
    
    #재생횟수 정렬
    playcount = {}
    for i, count in enumerate(plays):
        playcount[i] = count
        
    sortedcount = list(sorted(playcount, key = lambda x : -playcount[x]))
    #print(sortedcount)
    
    #재생 횟수에 따른 장르 정렬
    sortedgenres = {}
    total ={}
    for i in sortedcount:
        g = genres[i]
        if g not in sortedgenres:
            sortedgenres[g] = []
            total[g] = 0
        sortedgenres[g].append(i)
        total[g] += plays[i]
        
    
    #print(sortedgenres)
    
    for g in sorted(total, key=lambda g: -total[g]):    # ⭐ 총합 큰 장르부터
        for i, x in enumerate(sortedgenres[g]):
            if i <= 1:
                answer.append(x)
    
    
    
    return answer