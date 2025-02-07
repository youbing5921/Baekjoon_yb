n = int(input())

ans = 1

for i in range(1, n+1): # 단계
    ans += (i+1) * 3 - 2

print(ans % 45678)