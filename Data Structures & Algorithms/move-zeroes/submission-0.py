class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res = []
        for n in nums:
            if n != 0:
                res.append(n)
        while len(res) < len(nums):
            res.append(0)
        nums[:] = res