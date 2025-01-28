lst = list(map(int, input().split()))
sum = 0

for elt in lst:
    sum += elt*elt
sum %= 10

print(sum)