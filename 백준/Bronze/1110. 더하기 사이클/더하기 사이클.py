n = int(input())
if n < 10:
    a = 0
    b = n
else:
    a = n // 10
    b = n % 10
new = ""
res = 0
n = str(a)+str(b)
while n != new:
    temp = b
    b = (a+b) % 10
    a = temp
    new = str(a)+str(b)
    # print(new)
    res += 1
    
print(res)