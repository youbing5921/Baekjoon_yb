'''
# DFS는 미로 문제에서 시간복잡도가 급증
def dfs(x, y): # (x, y)에서 (m-1, n-1)까지 갈 수 있는 최소 경로를 반환
    if x == n-1 and y == m-1: # 도착
        return 1
    if x < 0 or x > n-1 or y < 0 or y > m-1 or maze[x][y] == 0: # 잘못된 경로
        return n*m*2
    maze[x][y] = 0
    res = 1 + min(dfs(x, y-1), dfs(x, y+1), dfs(x-1, y), dfs(x+1, y))
    maze[x][y] = 1  # 방문 복원
    return res

n, m = map(int, input().split())
maze = []
for i in range(n): # 미로 입력
    lst = list(map(int, input().strip()))
    maze.append(lst)
print(dfs(0, 0))
'''

from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    # visited[x][y]에는 (x, y)까지 가는데 걸린 거리를 표시
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1: # 종료 조건
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

print(bfs())