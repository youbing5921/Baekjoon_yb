import sys
input = sys.stdin.readline

n = int(input())
ans = 0

while n > 0:
    ans += 1
    if "666" in str(ans):
        n -= 1
print(ans)