import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
q = int(input())

prefix_sum = [0] * (n+1)
prev = 0
ans = []

# 누적합 구하기
# prefix_sum에는 0~i번째까지 연주했을 때 틀리는 횟수를 저장함.
# i+1번째까지 확인해서 i번째에 저장함.
for i in range(n-1):
    if array[i] > array[i+1]:
        prev += 1
    prefix_sum[i+1] = prev
prefix_sum[n] = prev

for i in range(q):
    x, y = map(int, input().split())
    ans.append(str(prefix_sum[y-1] - prefix_sum[x-1]))

print('\n'.join(ans))
