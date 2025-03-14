def dec(n):
    res = 0
    i = 1
    while n:
        res += (n % 10) * i
        n //= 10
        i *= 2
    return res

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = dec(a)
    b = dec(b)
    print(bin(a+b)[2:])
    