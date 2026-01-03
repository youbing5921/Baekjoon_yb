def solution(phone_book):
    answer = True
    dic = {} # key(번호 앞 부분) - value(번호 뒷 부분)
    l = len(min(phone_book, key=len)) # 길이가 가장 짧은 전화번호의 길이 찾기
    for p in phone_book:
        p1 = p[:l]
        p2 = p[l:] # 빈 문자열일 수 있음.
        if p1 in dic: # 이미 시작하는 번호가 같은 경우 -> 조건에 맞을 수 있음.
            pp2 = dic[p1]
            if len(p2) < len(pp2):
                if p2 == pp2[:len(p2)]:
                    return False
            else:
                if pp2 == p2[:len(pp2)]:
                    return False
        else: # 시작하는 번호가 같지 않음.
            dic[p1] = p2
    return answer