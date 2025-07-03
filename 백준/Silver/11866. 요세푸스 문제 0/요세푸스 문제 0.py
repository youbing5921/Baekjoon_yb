# n: 사람 수 / k: 간격
n, k = map(int, input().split())
array = list(range(1, n+1)) # 사람 테이블 구현
index = 0
ans = "<"

while n > 1:
    index = (index + k-1) % n # 제거할 사람의 인덱스 번호 구하기
    ans += str(array.pop(index)) + ", "
    n -= 1

ans += str(array.pop()) + ">"
print(ans)