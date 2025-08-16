def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
        return False
    if board[x][y] == -1:
        return True
    visited[x][y] = True
    step = board[x][y]
    return dfs(x+step, y) or dfs(x, y+step)
    


board = []
n = int(input())
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[False]*n for _ in range(n)]

if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")