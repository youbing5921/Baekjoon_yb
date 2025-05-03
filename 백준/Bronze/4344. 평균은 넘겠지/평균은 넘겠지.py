c = int(input())
ans_lst = []

for _ in range(c):
    lst = list(map(int, input().split()))
    n = lst.pop(0)
    avg = sum(lst) / n
    ans = 0
    for elt in lst:
        if elt > avg:
            ans += 1
    ans = str(format(round(ans / n * 100, 3), ".3f"))+"%"
    ans_lst.append(ans)

for answer in ans_lst:
    print(answer)