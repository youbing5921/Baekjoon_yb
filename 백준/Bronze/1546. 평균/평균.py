n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
new_lst = []

for elt in lst:
    new_lst.append(elt / m * 100)

print(sum(new_lst) / n)