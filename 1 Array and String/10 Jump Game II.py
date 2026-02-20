class Solution:
    def jump(self, nums: List[int]) -> int:
        target=len(nums)-1
        jumps=0
        while target:
            for i,n in enumerate(nums[:target]):
                if i+n>=target:
                    target=i
                    jumps+=1
                    break
        return jumps
