class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indicies={}
        for i in range(len(nums)):
            n=nums[i]
            if n in indicies and abs(indicies[n]-i)<=k:
                return True
            indicies[n]=i
        return False

