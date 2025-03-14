n = int(input())
a1 = a2 = 1
res = 0

if n <= 2: print(1)
else:
    for _ in range(n - 2):
        res = a1 + a2
        a1, a2 = a2, res

    print(res)