a, b = map(int, input().split())
c = int(input())

min = b + c
a += min // 60
a %= 24
b = min % 60

print(str(a) + " " + str(b))