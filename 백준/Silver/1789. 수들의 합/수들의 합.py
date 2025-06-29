s = int(input())
_sum = 0

# 1부터 차근차근 더하면서 1+ ... + k  <= S < 1 + ... + k+1인 k를 찾는다.
# 그러면 k개가 답이 됨.
if s == 1: print(1)
else:
    for i in range(1, s):
        _sum += i
        if _sum <= s < _sum+i+1:
            print(i)
            break