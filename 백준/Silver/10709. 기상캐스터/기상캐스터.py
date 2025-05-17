h, w = map(int, input().split())

for _ in range(h):
    cloud = input()
    ans = []
    minute = 0
    for elt in cloud:
        if elt == 'c':
            ans.append(0) # 처음부터 떠있었던 구름인 경우
            minute = 1 # 구름 이동시킬 준비
        elif minute == 0: # 이동시킬 구름이 없는 경우
            ans.append(-1)
        else: # 구름을 이동시키면 몇 분 후에 구름이 뜨는 경우
            ans.append(minute)
            minute += 1
    print(*ans)