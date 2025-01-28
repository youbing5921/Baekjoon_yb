lst = list(map(int, input().split()))

org = [1, 1, 2, 2, 2, 8]
ans = []

for i in range(len(lst)):
    ans.append(org[i]-lst[i])
print(*ans)