class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numD={}
        for i in nums:
            if not(i in numD):
                numD[i]=0
            numD[i]+=1
        
        threshold=len(nums)/2
        for k in numD:
            if numD[k]>threshold:
                return k
