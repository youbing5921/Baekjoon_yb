import sys
sys.setrecursionlimit(10000)  # 재귀 한도 늘리기

def dfs(x, y): # 애벌레가 보호하는 배추들을 소거한다.
    if x < 0 or x >= m or y < 0 or y >= n or field[x][y] == 0: # 종료 조건
        return
    else: # 상하좌우에 배추가 있는지 확인하여 소거한다.
        # 다른 dfs와 달리 상, 좌를 살펴보는 이유는 방향성이 없기 때문이다. 
        field[x][y] = 0
        dfs(x, y-1) # 상
        dfs(x, y+1) # 하
        dfs(x-1, y) # 좌
        dfs(x+1, y) # 우

for _ in range(int(input())):
    answer = 0
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)] # 밭 생성
    for i in range(k): # 배추 정보 저장
        x, y = map(int, input().split())
        field[x][y] = 1

    # 밭을 돌면서 배추에 근접한 배추들을 0으로 바꾸면서 한 애벌레가 보호하는 배추들을 소거한다.
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                answer += 1 # 애벌레 개수 증가
                dfs(i, j) # 소거
    print(answer)