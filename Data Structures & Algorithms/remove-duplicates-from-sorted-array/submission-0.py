class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        cur = 0
        while cur < len(nums):
            dup = cur + 1
            while dup < len(nums) and nums[dup] == nums[cur]:
                nums.pop(dup)
            cur = dup
        return cur
                

# 1 2 3 4
#   d
#   c  