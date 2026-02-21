class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lMul=[]
        rMul=[]
        lM,rM=1,1
        rev=nums[::-1]
        for i in range(len(nums)):
            lM*=nums[i]
            rM*=rev[i]
            lMul.append(lM)
            rMul.append(rM)
        rMul=rMul[::-1]
        
        res=[rMul[1]]
        for i in range(1,len(nums)-1):
            res.append(lMul[i-1]*rMul[i+1])
        res.append(lMul[-2])

        return res
