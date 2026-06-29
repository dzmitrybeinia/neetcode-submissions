class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        min_len = float('inf')
        cur = 0
        while r < len(nums):
            cur += nums[r]
            while cur >= target:
                min_len = min(min_len, r - l + 1)
                cur -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0

# 2,1,5,1,5,3
#     l
#         r

# cur = 11
# min = 3