import math

a, b, v = map(int, input().split())
length = 0

# while length < v:
#     length += a - b
#     day += 1

print(math.ceil((v-a) / (a-b))+1)