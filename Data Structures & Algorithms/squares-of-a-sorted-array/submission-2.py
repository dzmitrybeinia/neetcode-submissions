class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        cur = r
        res = [0] * len(nums)
        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            if left > right:
                res[cur] = left
                l += 1
            else:
                res[cur] = right
                r -= 1
            cur -=1
        return res