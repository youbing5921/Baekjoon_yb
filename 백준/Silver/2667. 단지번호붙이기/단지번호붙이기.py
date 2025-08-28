n = int(input())
field = [list(map(int, input().strip())) for _ in range(n)]
ans = []

def dfs(x, y): # 방문한 집들 0으로 바꾸고 그 개수를 셈.
    if x < 0 or x > n-1 or y < 0 or y > n - 1 or field[x][y] == 0: # 종료 조건
        return 0
    field[x][y] = 0 # 방문한 집 0으로 변경
    return 1 + dfs(x, y-1) + dfs(x, y+1) + dfs(x-1, y) + dfs(x+1, y) # 상하좌우에 있는 집들 확인

for x in range(n):
    for y in range(n):
        if field[x][y] == 1:
            building = dfs(x, y)
            ans.append(building)

ans.sort() # 오름차순 정렬
print(len(ans)) # 총 단지 수 출력
print(*ans, sep="\n") # 단지별 건물 수 출력