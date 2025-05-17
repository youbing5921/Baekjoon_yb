# 최대공약수(gcd)를 구해서 a * b = (gcd) * (lcm) 공식 사용
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    root = min(a, b)
    for i in range(root, 0, -1):
        if a % i == 0 and b % i == 0:
            print(a*b//i)
            break