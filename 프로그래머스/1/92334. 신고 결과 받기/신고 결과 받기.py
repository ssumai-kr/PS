from collections import defaultdict

def solution(id_list, report, k):
    count = defaultdict(int)          # 유저 → 신고당한 횟수 (중복 제외)
    reported = defaultdict(set)       # 신고한 사람 → 신고당한 사람들

    # 1) 신고 모으기
    for r in report:
        a, b = r.split()              # a가 b를 신고
        if b not in reported[a]:      # 처음 하는 신고만
            reported[a].add(b)
            count[b] += 1

    # 2) 유저마다 메일 수 세기
    answer = []
    for user in id_list:              # id_list 순서대로 반환
        mail = 0
        for target in reported[user]:
            if count[target] >= k:    # 내가 신고한 사람이 정지됐으면
                mail += 1
        answer.append(mail)
    return answer