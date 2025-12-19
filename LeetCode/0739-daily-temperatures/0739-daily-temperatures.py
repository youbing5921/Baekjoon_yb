class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 스택으로 구현
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and stack[-1][1] < cur_temp:
                prev_day, _ = stack.pop()
                answer[prev_day] = cur_day - prev_day
            stack.append((cur_day, cur_temp))
        return answer
        # 완전탐색으로 구현 -> 시간초과
        # n = len(temperatures)
        # answer = []
        # for i in range(n-1):
        #     if temperatures[i] < temperatures[i+1]: # 다음날이 더 따뜻하면
        #         answer.append(1)
        #     else: # 다음날이 더 추우면 더 따뜻해질 때까지 날을 찾아야 함.
        #         for j in range(i+2, n):
        #             if temperatures[i] < temperatures[j]:
        #                 answer.append(j-i)
        #                 break
        #         else: # 더 따뜻해지는 날이 없는 경우
        #             answer.append(0)

        # answer.append(0) # 마지막 날 추가
        # return(answer)