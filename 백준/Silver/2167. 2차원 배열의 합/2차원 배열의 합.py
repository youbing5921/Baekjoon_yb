n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 누적합 구하기
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_sum[i][j] = array[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    
    result = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
    print(result)
    
'''
n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = []

    for row in range(i-1, x):
        ans += array[row][j-1:y]
        # for col in range(j-1, y):
        #     ans += array[row][col]
    print(sum(ans))
'''
