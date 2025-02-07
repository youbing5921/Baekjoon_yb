a, b, c = map(int, input().split())

if(b >= c): print(-1)
else:
    cnt = a // (c-b) + 1

    if cnt < 1:
        print(-1)
    else:
        print(cnt)