class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in nums:
            cnt=nums.count(x)
            if cnt>2:
                for _ in range(cnt-2):
                    nums.remove(x)
        return len(nums)
