class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return None
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            return None

        endPos=m
        for i in range(n):
            nums1[endPos]=nums2[i]
            for di in range(endPos):
                if nums1[endPos-1-di]>nums1[endPos-di]:
                    nums1[endPos-1-di],nums1[endPos-di]=nums1[endPos-di],nums1[endPos-1-di]
                else:
                    break
            endPos+=1

