from itertools import combinations

def solution(relation):
    def check(small, big): # small이 big의 부분집합인지 확인
        for s in small:
            if s not in big:
                return False
        return True
    
    answer = 0
    key_list = [] # ex) (1, 2)
    row = len(relation)
    col = len(relation[0])
    
    for i in range(1, col+1):
        comb_list = list(combinations(list(range(col)), i)) # i개 원소로 인덱스 콤비네이션 만들기
        for comb in comb_list:
            for k in key_list: # 최소성을 만족할 수 있는 키인지 먼저 확인
                if check(k, comb):
                    break
            else:
                value = []
                for rel in relation:
                    v = []
                    for idx in range(col):
                        if idx in comb:
                            v.append(rel[idx])
                    value.append(tuple(v))
                if len(set(value)) == len(value): # key로 사용 가능
                    key_list.append(comb)
        
    return len(key_list)