amount_b = amount_t = int(input()) # 현금
shares_b = shares_t = 0 # 보유 주식 수
stock = list(map(int, input().split())) # 주가

for idx, price in enumerate(stock):
    # 준현이는 주식을 살 수 있다면 무조건 최대한 많이 산다.
    if amount_b >= price:
        shares_b += amount_b // price
        amount_b %= price
    
    # 성민이는 직전 3일동안 상승했다면 전량 매도한다.
    if idx > 2 and shares_t > 0 and stock[idx-3] < stock[idx-2] < stock[idx-1]:
        amount_t += shares_t * price
        shares_t = 0

    # 성민이는 직전 3일동안 하락했다면 전량 매수한다.
    if idx > 2 and stock[idx-3] > stock[idx-2] > stock[idx-1]:
        shares_t += amount_t // price
        amount_t %= price

amount_b += shares_b * stock[-1]
amount_t += shares_t * stock[-1]

if amount_b > amount_t:
    print("BNP")
elif amount_b == amount_t:
    print("SAMESAME")
else:
    print("TIMING")