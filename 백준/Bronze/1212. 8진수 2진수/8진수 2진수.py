a = input()

# 시간 초과
# ans = ""
# for elt in a:
#     elt = int(elt)
#     b = ""
#     for _ in range(3):
#         b = str(elt % 2) + b
#         elt //= 2
#     ans += b
# print(int(ans))

# 시간 초과
# ans = ""
# for elt in a:
#     elt = int(elt)
#     b = ""
#     b += str(elt // 4)
#     elt %= 4
#     b += str(elt // 2) + str(elt % 2)
#     ans += b
# print(int(ans))

# 시간 초과
# def to_binary(n):
#     return ("00" + bin(n)[2:])[-3:]  # '0b' 제거
# ans = ""
# for elt in a:
#     elt = int(elt)
#     elt = to_binary(elt)
#     print(elt)
#     ans += elt
# print(int(ans))

ans = []
for elt in a:
    elt = int(elt)
    b = ""
    for _ in range(3):
        b = str(elt % 2) + b
        elt //= 2
    ans.append(b)
print(int("".join(ans)))