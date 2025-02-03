a = int(input())
b = input()
res = 0

# for i in range(3):
#     elt = a * int(b[2 - i])
#     print(elt)
#     res += elt * 10 ** i

# print(res)


# 디벨롭 : ?자리수 x ?자리수
b_len = len(b)
for i in range(b_len):
    elt = a * int(b[b_len - 1 - i])
    print(elt)
    res += elt * 10 ** i

print(res)