class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for _ in range(len(nums)):
            numsD={}
            for x in nums:
                if not(x in numsD):
                    numsD[x]=0
                numsD[x]+=1
            
            for x in nums:
                if numsD[x]!=1:
                    nums.remove(x)

        return len(nums)
