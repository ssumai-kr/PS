def solution(phone_book):
    answer = True
    
    #한 번호가 다른 번호의 접두어인 경우가 있는지 확인
    s = set(phone_book)
    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in s:                # set 조회는 O(1)
                return False
    return True

    
    return answer