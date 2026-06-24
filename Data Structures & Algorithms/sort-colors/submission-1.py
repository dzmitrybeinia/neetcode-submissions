class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_zeros = 0
        count_ones = 0
        count_twos = 0
        for n in nums:
            if n == 0:
                count_zeros += 1
            elif n == 1:
                count_ones += 1
            else:
                count_twos += 1
        cur = 0
        while cur < count_zeros:
            nums[cur] = 0
            cur += 1
        while cur < count_zeros + count_ones:
            nums[cur] = 1
            cur += 1
        while cur < count_zeros + count_ones + count_twos:
            nums[cur] = 2
            cur += 1
        