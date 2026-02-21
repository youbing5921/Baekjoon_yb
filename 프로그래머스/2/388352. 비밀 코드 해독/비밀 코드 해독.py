from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    # 기준 리스트와 비교할 리스트가 주어지면 일치하는 개수 반환
    def system_response(std, lst):
        find = 0
        for elt in std:
            if elt in lst:
                find += 1
        return find
    
    for comb in combinations(range(1, n+1), 5): # nC5로 만들 수 있는 경우의 수 전부 검사
        for i in range(len(q)):
            if ans[i] != system_response(q[i], comb):
                break
        else: # 모든 경우가 맞음
            answer += 1
        
    return answer