class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {} # key(수열의 끝 숫자) - value(수열의 길이)
        nums.sort()
        for n in nums:
            if n-1 in dic: # 그 전 숫자가 있으면
                dic[n] = dic[n-1] + 1
            else: # 그 전 숫자가 없으면
                dic[n] = 1
        v = list(dic.values())
        if len(v) == 0:
            return 0
        else: return max(v)