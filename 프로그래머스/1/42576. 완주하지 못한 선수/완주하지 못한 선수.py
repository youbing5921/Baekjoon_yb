def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant: # 참가자들 딕셔너리에 추가
        if p in dic: # 동명이인이 있는 경우
            dic[p] += 1
        else:
            dic[p] = 1
    
    for c in completion:
        if dic[c] == 1: # 동명이인 없음.
            dic.pop(c)
        else: # 동명이인 있음.
            dic[c] -= 1
    
    return list(dic)[0]