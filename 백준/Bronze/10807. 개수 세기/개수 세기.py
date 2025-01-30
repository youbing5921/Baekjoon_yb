n = int(input())
lst = list(map(int, input().split()))
v = int(input())
ans = 0

for i in range(n):
    if lst[i] == v:
        ans += 1

print(ans)