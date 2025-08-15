n, m = map(int, input().split())

# 바닥에 가로로 놓을 타일이 몇 개 필요한지 세는 함수
# - 타일은 그냥 세면 되지만 ㅣ 타일은 세로로 놓아야 하기 때문에 floor를 뒤집어서 입력한다.
def check_tile(floor, standard):
    res = 0
    for line in floor:
        j = 0
        while j < len(line):
            if line[j] == standard:
                while j < len(line) and line[j] == standard:
                    j += 1
                res += 1
            else: j += 1
    return res
    

floor = []
res = 0

# 바닥 입력받기
for i in range(n):
    floor.append(list(input()))

# - 타일이 몇 개 쓰여야 하는지 조사
res += check_tile(floor, "-")

# | 타일이 몇 개 쓰여야 하는지 조사
reversed_floor = [[0] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        reversed_floor[j][i] = floor[i][j]
res += check_tile(reversed_floor, "|")

print(res)