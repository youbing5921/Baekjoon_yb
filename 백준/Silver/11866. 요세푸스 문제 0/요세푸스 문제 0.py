# n: 사람 수 / k: 간격
n, k = map(int, input().split())
array = list(range(1, n+1))
index = 0
ans = "<"

while n > 1:
    index = (index + k-1) % n
    ans += str(array.pop(index)) + ", "
    n -= 1

ans += str(array.pop()) + ">"
print(ans)