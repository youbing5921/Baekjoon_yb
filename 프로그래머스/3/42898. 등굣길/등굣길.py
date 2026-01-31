'''
구현 방식
- 강의에서 했던 것처럼 갈 수 있는 경우 세는데 puddles에 있으면 그 경로는 못 감
- 문제에 나온 격자와 같은 크기의 테이블을 하나 만들어서 0으로 모두 초기화
- dp[i][j] : (i, j)까지 갈 수 있는 경로의 수 반환
- base case : dp[1][1] = 1 / dp[1][j] = dp[1][j-1] / dp[i][1] = dp[i-1][1]
- recurrance : dp[i][j] = dp[i-1][j] + dp[i][j-1] ((i, j)가 puddles에 있으면 0)
'''
def solution(m, n, puddles):
    puddles = set(map(tuple, puddles))
    memo = [[-1] * (n + 1) for _ in range(m + 1)]

    def dp(i, j):
        if i < 1 or j < 1:
            return 0
        if (i, j) in puddles:
            return 0
        if i == 1 and j == 1:
            return 1
        if memo[i][j] != -1:
            return memo[i][j]

        memo[i][j] = (dp(i-1, j) + dp(i, j-1))
        return memo[i][j]

    return dp(m, n) % 1000000007