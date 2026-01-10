'''
# nums들로 res -> t를 만드는 경우의 수 반환
def make(nums, res, t):
    if len(nums) == 0:
        if res == t:
            return 1
        else:
            return 0
    
    return make(nums[1:], res + nums[0], t) + make(nums[1:], res - nums[0], t)
    
def solution(numbers, target):
    return make(numbers, 0, target) 
'''
# 슬라이싱 대신 인덱스 사용
def solution(numbers, target):
    def dfs(idx, res):
        if idx == len(numbers):
            return res == target
        return dfs(idx+1, res+numbers[idx]) + dfs(idx+1, res-numbers[idx])
    
    return dfs(0, 0)