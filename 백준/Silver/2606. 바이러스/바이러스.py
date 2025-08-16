com = int(input())
n = int(input())
network = [list(map(int, input().split())) for _ in range(n)]
ans = {1} # 바이러스에 걸린 컴퓨터 수
i = 0 # 조사한 횟수

while i < len(ans): # 바이러스에 걸린 컴퓨터들에 연결된 것들을 찾음.
    for a in network:
        if a[0] in ans or a[1] in ans:
            ans.add(a[0])
            ans.add(a[1])
    i += 1
print(len(ans)-1)