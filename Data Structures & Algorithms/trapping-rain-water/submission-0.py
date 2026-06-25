class Solution:
    def trap(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        l_max, r_max = 0, 0
        res = 0
        while l <= r:
            l_max = max(l_max, nums[l])
            r_max = max(r_max, nums[r])
            if nums[l] < nums[r]:
                res += min(l_max, r_max) - nums[l]
                l += 1
            else:
                res += min(l_max, r_max) - nums[r]
                r -= 1
        return res

# 0,2,0,3,1,0,1,3,2,1
# l                 
#                   r
# res = 0
# l_max = 0
# r_max = 1