class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target=len(nums)-1
        while target:
            for i,n in enumerate(nums[:target]):
                if i+n>=target:
                    target=i
                    break
            else:
                return False
        return True
