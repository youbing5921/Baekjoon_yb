a, b = map(int, input().split())

if a > b:
    a, b = b, a

ans = (b * (b+1) - (a-1) * a) / 2
print(int(ans))