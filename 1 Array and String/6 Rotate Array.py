class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N=len(nums)
        pointer=k%N
        nums[:]=nums[-pointer:]+nums[:-pointer]

