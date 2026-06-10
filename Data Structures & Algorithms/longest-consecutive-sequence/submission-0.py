class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in nums:
            cur = n
            seq = 0
            while cur in seen:
                seq += 1
                cur += 1
            longest = max(longest, seq)

        return longest