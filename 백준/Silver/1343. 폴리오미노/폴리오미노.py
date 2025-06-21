s = list(input())
idx = 0
x = 0

if s == ".":
    print(-1)
else:
    l = len(s)
    while idx < l:
        if s[idx] == "X": # 지금이 X이면
            while idx < l and s[idx] == "X": # .을 만날 때까지 반복문 돌기
                x += 1
                if x == 4: # x가 4개 모이면 AAAA로 바꾸기
                    s[idx-3:idx+1] = list("AAAA")
                    x = 0
                idx += 1
            # .을 만나서 반복문이 종료되면 남은 x의 개수가 2개일 때 BB로 바꾸고 아니면 프로그램 종료
            if x % 2:
                print(-1)
                exit(0)
            elif x == 2:
                s[idx-2:idx] = list("BB")
                x = 0
        idx += 1 # 지금이 X가 아니면 그냥 스킵
    print(''.join(s))