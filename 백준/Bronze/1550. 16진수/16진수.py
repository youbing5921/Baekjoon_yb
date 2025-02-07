a = input()
ans = 0
len_a = len(a)
for i in range(len_a):
    elt = a[len_a - i - 1]
    if ('A' <= elt <= 'F'):
        temp = ord(elt) - ord('A') + 10
    else:
        temp = int(elt)
    ans += temp * 16 ** i
print(ans)