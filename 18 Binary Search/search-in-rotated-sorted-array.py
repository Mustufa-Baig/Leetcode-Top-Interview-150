class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        # find the index of the smallest value using binary search
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        # lo == hi is the index of the smallest value and also the number of places rotated
        rot = lo
        lo, hi = 0, len(nums) - 1
        # The usual binary search and accounting for rotation
        while lo <= hi:
            mid = (lo + hi) // 2
            realmid = (mid + rot) % len(nums)
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
