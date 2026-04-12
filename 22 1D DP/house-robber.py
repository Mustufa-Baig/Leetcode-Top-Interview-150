class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base cases for 1 or 2 houses
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # result[i] stores the max money robbed up to house i
        result = [0] * (n + 1)

        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # Option 1: Rob this house (nums[i]) and add profit from i-2
            steal = nums[i] + result[i - 2]
            # Option 2: Skip this house and take profit from i-1
            skip = result[i - 1]

            result[i] = max(steal, skip)

        return result[n-1]