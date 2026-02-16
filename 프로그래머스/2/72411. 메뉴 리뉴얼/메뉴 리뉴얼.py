'''
1. course 길이만큼 orders에서 문자열을 자르고 나오는 수를 카운트
2. answer를 만들어서 문제 답 구하기

힌트
from itertools import combinations
comb = list(combinations("ABC", 2)) # [('A','B'), ('A','C'), ('B','C')]
'''
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        counter = {}
        
        for order in orders:
            order = sorted(order)
            comb_list = list(combinations(order, c))
            
            for comb in comb_list:
                target = "".join(comb)
                if target in counter:
                    counter[target] += 1
                else:
                    counter[target] = 1
        
        if not counter:
            continue
            
        maximum = max(counter.values())
        
        if maximum >= 2:
            for key, value in counter.items():
                if value == maximum:
                    answer.append(key)
            
    return sorted(answer)