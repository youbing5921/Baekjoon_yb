t = int(input())
ans = []

for i in range(t):
    a = sorted(list(map(int, input().split())), reverse=True)
    ans.append(str(a[2]))

print('\n'.join(ans))