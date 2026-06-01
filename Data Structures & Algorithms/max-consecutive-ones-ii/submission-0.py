class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 1
        l = 0
        r = 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                ones -= 1
            while ones < 0:
                if nums[l] == 0:
                    ones += 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

# 1 0 1 1 0
# l
#         r

# res = 4
# ones = -1