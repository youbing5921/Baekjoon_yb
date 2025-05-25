import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
prefix_sum = [0] * (n+1)

# 누적합 구하기
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + array[i-1]
# print(prefix_sum)

for _ in range(m):
    i, j = map(int, input().split())
    result = prefix_sum[j] - prefix_sum[i-1]
    print(result)