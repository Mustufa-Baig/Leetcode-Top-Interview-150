class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [nums[0]]
        
        for num in nums[1:]:
            if num > dp[-1]:
                dp.append(num)
            else:
                idx = bisect.bisect_left(dp, num)
                dp[idx] = num
        
        return len(dp)
