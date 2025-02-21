import math

n = int(input())
lst = list(map(int, input().split()))
ans = 0

for a in lst:
    if a != 1:
        for i in range(2, int(math.sqrt(a))+1):
            if a % i == 0: break
        else:
            ans += 1

print(ans)