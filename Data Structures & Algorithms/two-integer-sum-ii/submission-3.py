class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum > target:
                right -= 1
            else:
                left += 1
        return [-1,-1]