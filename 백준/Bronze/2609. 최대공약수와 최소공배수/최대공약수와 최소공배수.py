n, m = map(int, input().split())
if n > m:
    n, m = m, n
gcd = 0
for i in range(1, n+1):
    if n % i == 0 and m % i == 0:
        gcd = i
print(gcd)
print(n * m // gcd)