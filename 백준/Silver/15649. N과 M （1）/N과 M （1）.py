n, m = map(int, input().split())

def backTracking(perm):
    if len(perm) == m:
        print(*perm)
        return
    
    for i in range(1, n+1):
        if len(perm) > 0 and i in perm: # 가지치기 본인이랑 같은 수가 나오면 패스
            continue
        else:
            perm.append(i)
            backTracking(perm)
            perm.pop()

backTracking([])