class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        scanner, next_non_zero = 0, 0
        while scanner < len(nums):
            if nums[scanner] == 0:
                scanner += 1
            else:
                nums[scanner], nums[next_non_zero] = nums[next_non_zero], nums[scanner]
                next_non_zero += 1
                scanner += 1
                