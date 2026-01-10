'''
# DFS로 풀면 재귀를 3^k번 해야 해서 시간초과 남
# x로 y를 만드는 최소 연산 횟수를 반환하는 함수
# cnt : 지금까지의 연산 횟수
def make(x, y, n, cnt):
    if x > y: # 실패
        return -1
    if x == y: # 성공
        return cnt
    
    # case 1
    c1 = make(x+n, y, n, cnt+1)
    # case 2
    c2 = make(x*2, y, n, cnt+1)
    # case 3
    c3 = make(x*3, y, n, cnt+1)
    
    cnt_lst = [x for x in [c1, c2, c3] if x != -1]

    if len(cnt_lst) > 0:
        return min(cnt_lst)
    else: return -1
    
def solution(x, y, n):
    return make(x, y, n, 0)
'''
from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = set([x])
    
    while queue:
        cur, cnt = queue.popleft()
        
        if cur == y:
            return cnt
        
        for nxt in (cur+n, cur*2, cur*3):
            if nxt <= y and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt+1))
    return -1