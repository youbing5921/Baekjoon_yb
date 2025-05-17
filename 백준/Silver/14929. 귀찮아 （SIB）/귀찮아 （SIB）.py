n = int(input())
lst = list(map(int, input().split()))

'''
# 시간초과
ans = []

for a in range(n-1):
    for b in range(a+1, n):
        ans.append(lst[a] * lst[b])
print(sum(ans))
'''

'''
(a+b)^2 = a^2 + b^2 + 2(ab)
(a+b+c)^2 = a^2 + b^2 + c^2 + 2(ab + ac + bc)
(a+b+c+d)^2 = a^2 + b^2 + c^2 + d^2 + 2(ab + ac + ad + bc + bd + cd)
'''
ans = sum(lst) ** 2

for i in lst:
    ans -= i ** 2

print(ans//2)