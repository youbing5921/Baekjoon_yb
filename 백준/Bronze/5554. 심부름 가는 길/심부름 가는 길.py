hour = minute = 0

for _ in range(4):
    minute += int(input())

hour = minute // 60
minute %= 60

print(hour)
print(minute)
