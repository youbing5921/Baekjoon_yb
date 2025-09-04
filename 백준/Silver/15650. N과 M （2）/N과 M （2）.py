'''
# itertools - combinations 사용
from itertools import combinations

n, m = map(int, input().split())

num = list(range(1, n+1))
lst = combinations(num, m)

for i in lst:
    print(*i)
'''

# 백트래킹 (itertools 사용 X)
n, m = map(int, input().split())

def backTracking(perm): # perm : 현재까지 만든 수열을 담는 리스트
    if len(perm) == m: # 종료 조건 : n개 중 m개를 다 넣음.
        print(*perm)
        return
    for i in range(1, n+1):
        if len(perm) > 0 and perm[-1] >= i: # 가지치기 : 오름차순에 위배되는 경우는 제외 (ex. [2, 1])
            continue
        else:
            perm.append(i)
            backTracking(perm) # 다음 깊이로 들어감.
            perm.pop() # 탐색이 끝나면 원래 상태로 복구 (중요!!)

backTracking([])