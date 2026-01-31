'''
구현 방식
- dp[cnt] = N을 cnt번 사용해서 만들 수 있는 모든 값들의 집합
- answer : dp[1~7]까지 해보면서 number가 dp[cnt]에 있으면 cnt가 정답 없으면 -1
- dp[1] = {N} (N == number이면 바로 1 반환하고 문제 종료)
- dp[2] = {NN, N+N, N*N, 1}
- dp[3] = dp[1]=N dp[2]로 사칙연산 혹은 NNN
- dp[4] = dp[1] dp[3]으로 사칙연산 혹은 NNNN
'''
def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]  # dp[0]은 사용 안 함

    for i in range(1, 9):
        # 1️⃣ NNN...N (i번)
        dp[i].add(int(str(N) * i))

        # 2️⃣ dp[j] + dp[i-j]
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(b - a)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
                    if a != 0:
                        dp[i].add(b // a)

        # 3️⃣ 정답 체크
        if number in dp[i]:
            return i

    return -1