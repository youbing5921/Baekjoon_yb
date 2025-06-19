import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))
ans = []

while a and b:
    if a[0] < b[0]:
        ans.append(a.popleft())
    else:
        ans.append(b.popleft())

ans += list(a)  # 남은 원소들 추가
ans += list(b)

print(*ans)