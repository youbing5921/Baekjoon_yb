import math
def find(n): # 소수 찾기
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True
    
m = int(input())
n = int(input())
arr = []

for i in range(m, n+1):
    if(find(i)):
        arr.append(i)

if(not arr):
    print(-1)
else:
    print(sum(arr))
    print(arr[0])