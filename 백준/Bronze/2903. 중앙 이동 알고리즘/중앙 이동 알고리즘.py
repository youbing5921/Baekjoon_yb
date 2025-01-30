n = int(input())  # 시행 횟수
ans = 4  # 결과
line = 2  # 직전 시행에서 있던 선 개수
new_line = 0.5  # 시행하면서 추가되는 선 개수 (2^(시행-1))

for i in range(1, n+1):
    new_line *= 2
    ans += new_line * line * 2 + new_line * new_line
    line += new_line

print(int(ans))