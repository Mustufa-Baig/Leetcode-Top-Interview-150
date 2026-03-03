class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not(nums):
            return []
        ranges=[[nums[0]]]
        for n in nums[1:]:
            if n==ranges[-1][-1]+1:
                ranges[-1].append(n)
            else:
                ranges.append([n])
        for i in range(len(ranges)):
            r=ranges[i]
            if len(r)==1:
                ranges[i]=str(r[0])
            else:
                ranges[i]=str(r[0])+'->'+str(r[-1])
        return ranges
