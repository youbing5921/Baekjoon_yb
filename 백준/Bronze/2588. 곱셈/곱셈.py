a = int(input())
b = input()
res = 0

for i in range(3):
    elt = a * int(b[2 - i])
    print(elt)
    res += elt * 10 ** i

print(res)