a, b = map(int, input().split())
prefix_sum = 0
arr = [0]

# 배열 i번째에는 1~i번째까지의 수열의 합이 담겨있음.
for i in range(1, b+1):
    for j in range(i):
        prefix_sum += i
        arr.append(prefix_sum)

if a == 1:
    print(arr[b])
else:
    print(arr[b]-arr[a-1])