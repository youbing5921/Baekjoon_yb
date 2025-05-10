n = int(input())
lst = []
ans = []

# 데이터 입력 받기
for _ in range(n):
    lst.append(tuple(map(int, input().split())))

for target_i, target_elt in enumerate(lst): # 이 친구의 덩치 등수 찾기
    k = 1
    for i in range(n):
        if target_i != i: # 다른 사람과 비교해서
            # 본인보다 덩치가 큰 사람이라면 등수가 한 칸 내려감.
            if target_elt[0] < lst[i][0] and target_elt[1] < lst[i][1]:
                k += 1
    ans.append(k) # 결과 저장
print(*ans)