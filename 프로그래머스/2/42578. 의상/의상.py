def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes: # 종류별 의상 개수 카운트
        kind = c[1]
        if kind in dic: # 이미 같은 종류의 의상이 있음.
            dic[kind] += 1
        else: # 같은 종류 의상 없음.
            dic[kind] = 1
    
    key = list(dic) # 의상 종류 리스트
    if len(key) == 1: # 의상이 1종류만 있음.
        return dic[key[0]]
    else: # 의상이 여러 종류 있음.
        for k in key:
            answer *= dic[k] + 1

        answer -= 1
        return answer