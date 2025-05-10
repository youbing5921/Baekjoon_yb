n = int(input())
lst = []
ans = []

for _ in range(n):
    lst.append(tuple(map(int, input().split())))

for target_i, target_elt in enumerate(lst):
    k = 1
    for i in range(n):
        if target_i != i:
            if target_elt[0] < lst[i][0] and target_elt[1] < lst[i][1]:
                k += 1
    ans.append(k)
print(*ans)