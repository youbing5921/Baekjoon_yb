import sys
input = sys.stdin.readline

n = int(input()) # 거슬러야 하는 돈
coin = 0 # 동전 개수

if n < 2 or n == 3:
    print(-1)
else:
    coin += n // 5
    n = n % 5
    if n % 2 == 1: # 거슬러야 하는 돈이 홀수가 되면 2원으로 바꿀 수 없으므로 5원짜리 하나를 다시 바꾸기 전으로 돌림.
        coin -= 1
        n += 5
    coin += n // 2
    print(coin)